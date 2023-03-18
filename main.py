from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {"greeting": "Welcome to my first API!"}

@app.get('/packages')
def get_packages():
    return packages
