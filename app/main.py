from fastapi import FastAPI
import mysql.connector
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + MySQL in Docker!!!!!!"}

@app.get("/db-status")
def db_status():
    try:
        connection = mysql.connector.connect(
            host="db",  # コンテナ名
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        if connection.is_connected():
            return {"db_status": "connected"}
    except Exception as e:
        return {"db_status": "error", "details": str(e)}