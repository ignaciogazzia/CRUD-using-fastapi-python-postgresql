import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from DataLayer.DAO_Product import ProductDAO
from BusinessLogic.Product import *

app = FastAPI()


@app.get('/')
def read_root():
    return {"greeting": "Welcome to my first API for Products and Packages!"}


@app.get('/products')
async def get_products():
    products = ProductDAO.show_products()
    return [product.to_dict() for product in products]


@app.get('/products/{product_id}')
async def get_product_by_id(product_id: int):
    product = ProductDAO.show_product(product_id)
    if product is None:
        return {}
    return product.to_dict()


@app.put('/products/{product_id}')
async def update_product_title(product_id: int, product: Producto):
    return ProductDAO.update_product(product_id, product.title)

