from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Backend!"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/add")
def add(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}


@app.get("/multiply")
def multiply(a: int, b: int):
    return {"a": a, "b": b, "multiply": a * b}


@app.get("/concatinate")
def concate(a: str, b: int):
    return {"a": a, "b": b, "concatinate": a + b}


@app.get("/square/{n}")
def square(n: int):
    return{"n": n, "square": n * n}


@app.get("/info")
def info(name: str, city: str, skills: str):
    return{"name": name, "city": city, "skills": skills.split(",")}


@app.get("/time")
def time():
    return{datetime.now().isoformat()}
