from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return { "Hello" : "World"}

@app.get("/platzi")
def platzi():
    return { "Hello" : "World"}