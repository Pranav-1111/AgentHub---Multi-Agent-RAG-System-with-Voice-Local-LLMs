# test_db.py

import os
import mysql.connector
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get credentials
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD") or ""
database = os.getenv("DB_NAME")

try:
    # Connect to DB
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = connection.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    print(f"✅ Connected to MySQL database `{database}` successfully!")
    print("📋 Tables in database:")
    for table in tables:
        print(f" - {table[0]}")

    cursor.close()
    connection.close()

except Exception as e:
    print("❌ Error connecting to MySQL:")
    print(e)
