from fastapi import FastAPI
import connection


app = FastAPI()


@app.get("/")
async def root():
    print(connection.con)
    return {"message": "Hello World"}

