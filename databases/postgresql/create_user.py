#!/usr/bin/env python3
"""
Script to connect to PostgreSQL and execute create_user.sql to set up an app schema and user.
Uses psycopg3 for PostgreSQL connectivity.
"""

import argparse
import getpass
import os
import sys
from pathlib import Path

import psycopg


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Create PostgreSQL app schema and user"
    )
    parser.add_argument("--host", default="localhost", help="PostgreSQL host")
    parser.add_argument("--port", type=int, default=5432, help="PostgreSQL port")
    parser.add_argument("--dbname", required=True, help="Database name")
    parser.add_argument("--user", required=True, help="PostgreSQL admin username")
    parser.add_argument("--password", help="PostgreSQL admin password")
    return parser.parse_args()


def execute_sql_file(connection, sql_file_path):
    """
    Execute SQL file and return status signal from RAISE NOTICE outputs.

    Returns:
        str: 'created' if user was created, 'existed' if user already existed
    """
    result_status = "unknown"

    # Read SQL file
    with open(sql_file_path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    # Create a list to capture notices
    notices = []

    # Define notice handler callback
    def notice_handler(diag):
        # In psycopg3, diag is a Diagnostic object with message attribute
        notices.append(diag.message)

    # Create a cursor and execute with notice handling
    connection.add_notice_handler(notice_handler)

    with connection.cursor() as cursor:
        cursor.execute(sql_script)
        connection.commit()

    # Process notices to extract the result status
    for notice in notices:
        if notice.startswith("RESULT:"):
            result_status = notice.replace("RESULT:", "").strip()
            break

    return result_status


def main():
    """Main function to connect to PostgreSQL and execute SQL file."""
    args = parse_arguments()

    # Get password from environment or prompt if not provided
    password = args.password or os.environ.get("PGPASSWORD")
    if not password:
        password = getpass.getpass(f"Password for {args.user}: ")

    # Get the path to the SQL file
    sql_file_path = Path(__file__).parent / "create_user.sql"
    if not sql_file_path.exists():
        print(f"Error: SQL file not found at {sql_file_path}")
        sys.exit(1)

    # Connect to PostgreSQL
    try:
        # In psycopg3, we can use conninfo string or parameters
        connection = psycopg.connect(
            host=args.host,
            port=args.port,
            dbname=args.dbname,
            user=args.user,
            password=password,
        )

        # Execute SQL file and get result status
        status = execute_sql_file(connection, sql_file_path)

        # Close the connection
        connection.close()

        # Decide next action based on status
        if status == "created":
            print("User was newly created. Proceeding with initial setup...")
            # Add your initialization code here
        elif status == "existed":
            print("User already existed. Skipping initialization...")
            # Add your existing user code here
        else:
            print(f"Unexpected status: {status}")
            sys.exit(1)

        # Return status as exit code (0=success, can be used by calling scripts)
        return 0

    except psycopg.Error as e:
        print(f"Database error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
