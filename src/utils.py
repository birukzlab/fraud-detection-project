# src/utils.py

import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def connect_to_db():
    """Connect to the PostgreSQL database using credentials from environment variables."""
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        print("Connection to PostgreSQL DB successful")
        return connection
    except Exception as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None

def close_connection(connection):
    """Close the PostgreSQL database connection."""
    if connection:
        connection.close()
        print("PostgreSQL connection is closed")

