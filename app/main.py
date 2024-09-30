from typing import Union

from fastapi import FastAPI
import psycopg2

import os

app = FastAPI()

PORT = os.environ["PORT"]

db = psycopg2.connect(host='localhost', dbname='testdb',user='postgres',password='password',port=PORT)

cursor=db.cursor()

@app.get("/")
def read_root():
    print(db)
    return {"Hello": "하이"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": f"아이템 번호: {item_id}"}