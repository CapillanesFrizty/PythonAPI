from fastapi import FastAPI
import connection

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/clients")
async def get_clients():
    sqlQuery = "SELECT * FROM clients"

    connection.my_cursor.execute(sqlQuery)
    result = connection.my_cursor.fetchall()

    return result