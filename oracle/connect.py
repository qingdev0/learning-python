#!/usr/bin/env python3
"""
This script demonstrates how to connect to an Oracle Database using Python 3.13,
based on a YAML configuration file that stores multiple database entries. If
the configuration for the chosen database alias contains a 'wallet_location',
SSL (TCPS) will be used automatically. Otherwise, a standard (non-SSL) connection
over TCP will be established.

Additionally, SQL files are parsed using 'sqlparse' to handle multiple statements
cleanly, without relying on naive string splits.

Usage example (command line):
  python main.py --config db_config.yaml --dbalias DevDB --sqlfile setup_table.sql

Requirements:
  - pip install pyyaml oracledb sqlparse
"""

import argparse
import os
import yaml
import oracledb
import sqlparse
from typing import List, Dict, Any, Optional
import socket
import subprocess
from pathlib import Path


def load_yaml_config(config_path: str) -> Dict[str, Any]:
    """
    Load the YAML file and return its contents as a dictionary.
    The YAML is expected to have a structure like:

      databases:
        DevDB:
          host: "127.0.0.1"
          port: 1521
          service_name: "ORCL"
          user: "scott"
          password: "tiger"
          # Optionally if SSL is needed, include:
          wallet_location: "/path/to/wallet"

        ProdDB:
          host: "10.0.0.5"
          port: 1522
          service_name: "PROD"
          user: "admin"
          password: "secret"
          wallet_location: "/path/to/prod_wallet"
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Cannot find config file: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)

    return content


def load_sql_file(sql_file_path: str) -> str:
    """Read the entire content of the given SQL file into a string."""
    if not os.path.exists(sql_file_path):
        raise FileNotFoundError(f"SQL file not found: {sql_file_path}")

    try:
        # Try UTF-8 first
        with open(sql_file_path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        # Fallback to system default encoding
        with open(sql_file_path, "r") as f:
            return f.read()


def split_sql_statements(sql_script: str) -> List[str]:
    """Split SQL script into individual statements, properly handling PL/SQL blocks."""
    statements = []
    current_statement = []
    in_plsql_block = False

    # First, use sqlparse to do basic statement splitting
    raw_stmts = sqlparse.split(sql_script)

    for statement in raw_stmts:
        # Skip empty statements
        if not statement.strip():
            continue

        # Check if this is the start of a PL/SQL block
        upper_stmt = statement.strip().upper()
        if upper_stmt.startswith("DECLARE") or upper_stmt.startswith("BEGIN"):
            in_plsql_block = True
            current_statement = [statement]
        # Check if this is the end of a PL/SQL block
        elif in_plsql_block:
            current_statement.append(statement)
            if "END;" in statement.upper():
                # Join the PL/SQL block parts and add to statements
                full_stmt = "\n".join(current_statement)
                statements.append(full_stmt)
                current_statement = []
                in_plsql_block = False
        else:
            # Regular SQL statement
            statements.append(statement)

    # Handle any remaining PL/SQL block
    if current_statement:
        statements.append("\n".join(current_statement))

    return [stmt.strip() for stmt in statements if stmt.strip()]


def test_network_connectivity(host: str, port: int) -> None:
    """Test basic network connectivity to the host and port."""
    try:
        socket.create_connection((host, port), timeout=5)
        print(f"✓ Successfully connected to {host}:{port}")
    except socket.timeout:
        print(f"✗ Connection timeout to {host}:{port}")
    except ConnectionRefusedError:
        print(f"✗ Connection refused to {host}:{port}")
    except Exception as e:
        print(f"✗ Failed to connect to {host}:{port}: {e}")


def inspect_wallet(wallet_location: str) -> None:
    """Inspect wallet contents and verify required files for Thin mode."""
    wallet_path = Path(wallet_location)
    if not wallet_path.exists():
        print(f"✗ Wallet directory not found: {wallet_location}")
        return

    print(f"\nWallet contents in {wallet_location}:")
    # Key files needed for python-oracledb Thin mode
    required_files = {
        "tnsnames.ora": "Network service names mapping",
        "ewallet.pem": "SSL certificates for mTLS authentication",
    }

    # Optional but useful files
    helpful_files = {
        "sqlnet.ora": "Network configuration parameters",
        "cwallet.sso": "Auto-login wallet (not used in Thin mode)",
        "ojdbc.properties": "JDBC connection properties",
    }

    found_files = set()

    try:
        wallet_files = list(wallet_path.glob("*"))
        print("\nRequired files for Thin mode:")
        for file in wallet_files:
            if file.name in required_files:
                print(f"✓ {file.name:<12} - {required_files[file.name]}")
                found_files.add(file.name)

        print("\nOther relevant files:")
        for file in wallet_files:
            if file.name in helpful_files:
                print(f"- {file.name:<12} - {helpful_files[file.name]}")

        missing_files = set(required_files.keys()) - found_files
        if missing_files:
            print("\n✗ Missing required files for Thin mode:")
            for file in missing_files:
                print(f"  - {file}")
        else:
            print("\n✓ All required files for Thin mode present")

    except Exception as e:
        print(f"✗ Failed to list wallet contents: {e}")


def connect_to_oracle(db_info: Dict[str, Any]) -> oracledb.Connection:
    """Connect to Oracle with enhanced diagnostics."""
    user = db_info.get("user")
    password = db_info.get("password")
    host = db_info.get("host")
    port = db_info.get("port")
    service_name = db_info.get("service_name")
    wallet_location = db_info.get("wallet_location")
    config_dir = db_info.get("config_dir")
    wallet_password = db_info.get("wallet_password")
    is_cloud = db_info.get("is_cloud", False)

    if not all([user, password, host, port, service_name]):
        raise ValueError(
            "Missing required database fields (user, password, host, port, service_name)."
        )

    # Diagnostic information
    print("\n=== Diagnostic Information ===")
    print(f"Connection details:")
    print(f"- Host: {host}")
    print(f"- Port: {port}")
    print(f"- Service: {service_name}")
    print(f"- User: {user}")
    print(f"- Wallet: {'Enabled' if wallet_location else 'Disabled'}")

    # Test network connectivity
    print("\nTesting network connectivity...")
    test_network_connectivity(host, port)

    # Check wallet contents if using wallet
    if wallet_location:
        inspect_wallet(wallet_location)

    # For cloud connections, we use the service name from tnsnames.ora
    if is_cloud:
        dsn = service_name  # Use the service name directly as DSN
    else:
        dsn = f"{host}:{port}/{service_name}"

    connect_args = {"user": user, "password": password, "dsn": dsn}

    if is_cloud:
        print("\nAttempting Oracle Cloud connection with mTLS...")
        if not wallet_location:
            raise ValueError("Wallet location is required for Oracle Cloud connections")

        # Configure for Oracle Cloud connection in Thin mode
        connect_args.update(
            {
                "config_dir": config_dir
                or wallet_location,  # Directory containing tnsnames.ora
                "wallet_location": wallet_location,  # Directory containing ewallet.pem
                "wallet_password": wallet_password,
                "ssl_server_dn_match": True,  # Enable DN matching for security
            }
        )
    elif wallet_location:
        print("\nAttempting SSL/TLS (TCPS) connection...")
        connect_args.update(
            {"wallet_location": wallet_location, "ssl_server_dn_match": False}
        )
    else:
        print("\nAttempting standard TCP connection...")

    try:
        conn = oracledb.connect(**connect_args)
        print("✓ Connection established successfully")

        # Test the connection with a simple query
        with conn.cursor() as cursor:
            try:
                cursor.execute("SELECT 1 FROM DUAL")
                cursor.fetchone()
                print("✓ Database query test successful")
            except oracledb.Error as e:
                print(f"✗ Database query test failed: {e}")
                raise

        return conn
    except oracledb.OperationalError as e:
        print(f"\n✗ Oracle connection failed (network/operational error):")
        print(f"Error message: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Check if the database server is running")
        print("2. Verify network connectivity (ping the host)")
        print("3. Check firewall settings")
        print(f"4. Verify the service '{service_name}' is running")
        raise
    except oracledb.DatabaseError as e:
        print(f"\n✗ Oracle connection failed (database error):")
        print(f"Error message: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Verify the database credentials")
        print("2. Check if the user account is locked")
        print("3. Verify the service name is correct")
        raise
    except Exception as e:
        print(f"\n✗ Oracle connection failed:")
        print(f"Error message: {str(e)}")
        print("\nPossible solutions:")
        print("1. Verify the wallet files are valid and not corrupted")
        print("2. Check if the service is available and accepting connections")
        print("3. Verify the database credentials are correct")
        print("4. Ensure the network/firewall allows TCPS connections")
        raise


def format_value(value, width=20):
    """Format a value for display, handling None and long strings."""
    if value is None:
        return "NULL".ljust(width)
    return str(value)[:width].ljust(width)


def run_diagnostics(conn: oracledb.Connection) -> None:
    """Run diagnostic queries and display results."""
    diagnostic_queries = [
        (
            "Database Time",
            """
            SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') AS DB_TIME FROM DUAL
        """,
        ),
        (
            "Session Information",
            """
            SELECT 
                SYS_CONTEXT('USERENV', 'SESSION_USER') AS USERNAME,
                SYS_CONTEXT('USERENV', 'DB_NAME') AS DB_NAME,
                SYS_CONTEXT('USERENV', 'SERVER_HOST') AS HOST_NAME,
                SYS_CONTEXT('USERENV', 'IP_ADDRESS') AS CLIENT_IP,
                SYS_CONTEXT('USERENV', 'OS_USER') AS OS_USER
            FROM DUAL
        """,
        ),
        (
            "Database Version",
            """
            SELECT BANNER AS VERSION FROM V$VERSION WHERE BANNER LIKE 'Oracle%'
        """,
        ),
        (
            "Instance Information",
            """
            SELECT 
                SYS_CONTEXT('USERENV', 'INSTANCE_NAME') AS INSTANCE_NAME,
                SYS_CONTEXT('USERENV', 'DB_UNIQUE_NAME') AS DB_UNIQUE_NAME
            FROM DUAL
        """,
        ),
    ]

    cursor = conn.cursor()

    print("\n=== Database Connection Diagnostics ===\n")

    for title, query in diagnostic_queries:
        print(f"\n--- {title} ---")
        try:
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if rows:
                # Calculate column widths
                col_widths = [len(col) for col in columns]
                for row in rows:
                    for i, value in enumerate(row):
                        col_widths[i] = max(col_widths[i], len(str(value or "NULL")))

                # Print header
                header = " | ".join(
                    col.ljust(width) for col, width in zip(columns, col_widths)
                )
                separator = "-" * len(header)
                print("\n" + header)
                print(separator)

                # Print rows
                for row in rows:
                    formatted_row = []
                    for value, width in zip(row, col_widths):
                        if value is None:
                            formatted_value = "NULL".ljust(width)
                        elif isinstance(value, (int, float)):
                            formatted_value = str(value).rjust(width)
                        else:
                            formatted_value = str(value).ljust(width)
                        formatted_row.append(formatted_value)
                    print(" | ".join(formatted_row))
            else:
                print("No data returned")

        except Exception as e:
            print(f"Error executing query: {str(e)}")

    cursor.close()


def execute_sql_file(conn: oracledb.Connection, sql_file: str = None) -> None:
    """Execute SQL file or run diagnostics."""
    try:
        # First run diagnostics
        run_diagnostics(conn)

        # Then execute SQL file if provided
        if sql_file:
            print(f"\n=== Executing {sql_file} ===\n")
            # ... rest of your SQL file execution code ...

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        conn.close()
        print("\nConnection closed.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Connect to an Oracle Database and run diagnostics."
    )
    parser.add_argument(
        "--config",
        default="connections.yaml",
        help="Path to the YAML config file (default: connections.yaml)",
    )
    parser.add_argument(
        "--database",
        required=True,
        help="Alias of the database entry in the YAML file.",
    )

    args = parser.parse_args()

    # 1) Load the YAML config
    config_data = load_yaml_config(args.config)
    databases_section = config_data.get("databases", {})
    db_info = databases_section.get(args.database)
    if not db_info:
        raise ValueError(f"Database alias '{args.database}' not found in config file.")

    # 2) Connect to Oracle and run diagnostics
    try:
        connection = connect_to_oracle(db_info)
        print("\n=== Connection successful! ===")

        # Run diagnostics
        run_diagnostics(connection)

    except oracledb.Error as e:
        print(f"Oracle Error: {e}")
        if "connection" in locals():
            connection.rollback()
    except Exception as e:
        print(f"General Error: {e}")
    finally:
        if "connection" in locals() and connection is not None:
            try:
                connection.close()
                print("\nConnection closed.")
            except oracledb.Error:
                pass  # Ignore errors during connection close


if __name__ == "__main__":
    main()
