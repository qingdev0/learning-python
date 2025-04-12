#!/usr/bin/env python3
"""
Oracle Database connection script using python-oracledb in thin mode.
Supports both regular TCP and SSL/TCPS connections.

Usage:
  python connect.py --config connections.yaml --database DevDB
"""

import argparse
import os
import socket
from pathlib import Path
from typing import Any, Dict

import oracledb
import yaml


def load_yaml_config(config_path: str) -> Dict[str, Any]:
    """Load database configuration from YAML file."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_network_connectivity(host: str, port: int) -> None:
    """Test basic network connectivity to the database."""
    try:
        socket.create_connection((host, port), timeout=5)
        print(f"✓ Network connectivity test successful")
    except Exception as e:
        print(f"✗ Network connectivity test failed: {str(e)}")


def inspect_wallet(wallet_location: str) -> None:
    """Verify wallet contents for SSL connections."""
    wallet_path = Path(wallet_location)
    if not wallet_path.exists():
        raise FileNotFoundError(f"Wallet directory not found: {wallet_location}")

    required_files = ["tnsnames.ora", "ewallet.pem"]
    missing_files = []

    for file in required_files:
        if not (wallet_path / file).exists():
            missing_files.append(file)

    if missing_files:
        raise FileNotFoundError(
            f"Missing required wallet files: {', '.join(missing_files)}"
        )


def connect_to_oracle(db_info: Dict[str, Any]) -> oracledb.Connection:
    """Connect to Oracle Database using thin mode."""
    # Extract connection parameters
    user = db_info.get("user")
    password = db_info.get("password")
    host = db_info.get("host")
    port = db_info.get("port")
    service_name = db_info.get("service_name")
    wallet_location = db_info.get("wallet_location")
    is_cloud = db_info.get("is_cloud", False)
    use_ssl = db_info.get("use_ssl", False) or is_cloud

    # Validate required parameters
    if not all([user, password, host, port, service_name]):
        raise ValueError("Missing required connection parameters")

    # Test network connectivity
    test_network_connectivity(host, port)

    try:
        if is_cloud or use_ssl:
            # SSL connection (cloud or on-premises)
            if not wallet_location:
                raise ValueError("Wallet location is required for SSL connections")
            inspect_wallet(wallet_location)

            connect_args = {
                "user": user,
                "password": password,
                "dsn": (
                    service_name
                    if is_cloud
                    else f"(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST={host})(PORT={port}))(CONNECT_DATA=(SERVICE_NAME={service_name})))"
                ),
                "wallet_location": wallet_location,
                "ssl_server_dn_match": True,
            }

            # Add config_dir for cloud connections
            if is_cloud:
                connect_args["config_dir"] = wallet_location
        else:
            # Basic TCP connection
            connect_args = {
                "user": user,
                "password": password,
                "dsn": f"{host}:{port}/{service_name}",
            }

        return oracledb.connect(**connect_args)

    except Exception as e:
        print(f"Connection failed: {str(e)}")
        raise


def run_basic_test(conn: oracledb.Connection) -> None:
    """Run a basic connection test."""
    with conn.cursor() as cursor:
        cursor.execute(
            """
            SELECT 
                TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') AS CURRENT_TIME,
                SYS_CONTEXT('USERENV', 'SESSION_USER') AS USERNAME,
                SYS_CONTEXT('USERENV', 'DB_NAME') AS DB_NAME,
                BANNER AS VERSION 
            FROM V$VERSION 
            WHERE BANNER LIKE 'Oracle%'
        """
        )
        result = cursor.fetchone()
        if result:
            time, user, db_name, version = result
            print("\nConnection Test Results:")
            print(f"Time: {time}")
            print(f"User: {user}")
            print(f"Database: {db_name}")
            print(f"Version: {version}")


def main() -> None:
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Connect to Oracle Database and verify connection."
    )
    parser.add_argument(
        "--config", default="connections.yaml", help="Path to the YAML config file"
    )
    parser.add_argument(
        "--database", required=True, help="Database alias from config file"
    )

    args = parser.parse_args()

    try:
        # Load configuration
        config = load_yaml_config(args.config)
        db_info = config.get("databases", {}).get(args.database)
        if not db_info:
            raise ValueError(f"Database '{args.database}' not found in config")

        # Establish connection
        print(f"\nConnecting to {args.database}...")
        conn = connect_to_oracle(db_info)
        print("✓ Connection established")

        # Run basic test
        run_basic_test(conn)

    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise
    finally:
        if "conn" in locals():
            conn.close()
            print("\nConnection closed")


if __name__ == "__main__":
    main()
