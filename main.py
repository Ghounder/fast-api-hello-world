from ast import Str
from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI,Body, Query

app = FastAPI()

#Models

class person(BaseModel):
    first_name : str
    last_name : str
    age : int
    hair_color : Optional[str] = None
    is_married : Optional[bool] = None

@app.get("/")
def home():
    return { "Hello" : "World"}

@app.get("/platzi")
def platzi():
    return { "Hello" : "World"}

#request and response body

@app.post("/person/new")
def create_person(person : person = Body(...)):
    return person

#validaciones query parameters

@app.get("/person/detail")
def show_person(
    name : Optional[str] = Query(None, min_length = 1, max_length = 50),
    age : int = Query(...)    
):
    return {name : age}
