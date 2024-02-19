from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel
import math 
app = FastAPI()

@app.get("/")
async def root():
    return{"hello": "world"}
class num(BaseModel):
    number: int

@app.get("/square/{number}")
async def square(number:int):
    if number < 10 or number > 100:
        raise HTTP(status_code= 400, exam = "number should be ranged")
    square_root = math.sqrt(number)
    return {"sqaure_root": square_root}