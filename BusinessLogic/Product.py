import datetime
from logger import log
from pydantic import BaseModel


class Product:

    def __init__(self, product_id=None, title=None, created_at=None):
        self._product_id = product_id
        self._title = title
        self._created_at = created_at

    def __str__(self):
        return f'ID {self._product_id} | TITLE: {self._title} | CREATED AT {self._created_at}  '

    def to_dict(self):
        return {
            'id': self._product_id,
            'title': self._title,
            'created_at': self._created_at.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        }

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self.title = title

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at


class Producto(BaseModel):
    product_id: int | None = None
    title: str
    created_at: datetime.datetime | None = None

    @classmethod
    def to_dict(cls, product: tuple):
        return {
            'product_id': product[0],
            'title': product[1],
            'created_at': product[2].strftime('%Y-%m-%d %H:%M:%S %Z%z')
        }


if __name__ == '__main__':
    product1 = Product('1', 'Motosierra', '17/03/2023')
    log.debug(product1)
