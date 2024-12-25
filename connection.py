import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

con = psycopg2.connect(
  host= os.getenv("DB_PG_HOST"),
  user= os.getenv("DB_PG_USER"),
  password=os.getenv("DB_PG_PASSWORD"),
  database= os.getenv("DB_PG_NAME"),
  port = os.getenv("DB_PG_PORT"),
)

my_cursor = con.cursor()

print(con)
