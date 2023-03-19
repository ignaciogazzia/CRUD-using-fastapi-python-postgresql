import json
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from DataLayer.DAO_Product import ProductDAO

app = FastAPI()


@app.get('/')
def read_root():
    return {"greeting": "Welcome to my first API for Products and Packages!"}


@app.get('/products')
def get_products():
    products = ProductDAO.show_products()
    return [product.to_dict() for product in products]
