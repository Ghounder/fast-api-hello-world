from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI,Body, Path, Query

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
    name : Optional[str] = Query(
        None,
        min_length = 1,
        max_length = 50,
        title = "person name",
        description = "This is the person name , between 1 to 50 char"
        ),
    age : int = Query(
        ...,
        title = "person age",
        description = "this is the person age, is required"
        )    
):
    return {name : age}

#validacione spath parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id : int = Path(
        ...,
        gt = 0,
        title = "person id",
        description = "this is the id of the person"
        )
):
    return { person_id : "exists"}