from typing import Optional
from enum import Enum
from datetime import date


from pydantic import BaseModel, EmailStr,Field, ListUniqueItemsError

from fastapi import FastAPI,Body, Path, Query

app = FastAPI()

#Models
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    yellow = "blonde"
    red = "red"


class Person(BaseModel):
    first_name : str = Field(
        ...,
        min_length= 1,
        max_length= 50,
        example = "Luis"
    )
    last_name : str = Field(
        ...,
        min_length= 1,
        max_length= 50,
        example = "Pozo"
    )
    age : int = Field(
        ...,
        gt= 0,
        lt= 115,
        example = 15
    )
    email : EmailStr = Field(
        ...
    )
    birth_date : date = Field(
        ...
    )
    hair_color : Optional[HairColor] = Field(default=None, example = "black")
    is_married : Optional[bool] = Field(default=None, example = "True")
    class Config:
        schema_extra = {
            "example" : {
                "first_name" : "Luis",
                "last_name" : "Pozo",
                "age" : "23",
                "hair_color" : "black",
                "is_married" : "True"
            }
        }

class Location (BaseModel):
    city : str = Field(
        ...,
        max_length=50,
        min_length=1
        )
    state : str = Field(
        ...,
        max_length=50,
        min_length=1
        )
    country : str = Field(
        ...,
        max_length=50,
        min_length=1
        )
    class Config:
        schema_extra = {
            "example" : {
                "city" : "example",
                "state": "example",
                "country":"examlp"
            }
        }


@app.get("/")
def home():
    return { "Hello" : "World"}

@app.get("/platzi")
def platzi():
    return { "Hello" : "World"}

#request and response body

@app.post("/person/new")
def create_person(person : Person = Body(...)):
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
#validations request body

@app.put("/person/{person_id}")
def update_person(
    person_id : int = Path(
        ...,
        title = "person id",
        description = "this is the person id",
        gt = 0
    ),
    person : Person = Body(
        ...
    ),
    location : Location = Body(
        ...
    )
):
    results = person.dict()
    results.update(location.dict())
    return person