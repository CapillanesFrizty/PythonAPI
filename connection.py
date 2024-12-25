import os
import psycopg2

DB_HOST = os.getenv("DB_PG_HOST")
DB_USER = os.getenv("DB_PG_USER")
DB_PASSWORD = os.getenv("DB_PG_PASSWORD")
DB_NAME = os.getenv("DB_PG_NAME")
DB_PORT = os.getenv("DB_PG_PORT", 5432)

try:
    con = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT,
    )
    print("Database connection successful")

    my_cursor = con.cursor()
except Exception as e:
    print(f"Error connecting to the database: {e}")
