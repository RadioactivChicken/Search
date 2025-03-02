#!/bin/python3.12
from fastapi import FastAPI
import database as db

app = FastAPI()

@app.get("/search/{key}")
async def read_item(key):

    result = db.search(key)

    return result

@app.get("/add/{key}/{url}")
async def read_item(key: str, url: str):

    result = db.add(key, url)
    return result
