from logger import log
from Services.DBConnection import DBConnection
from BusinessLogic.Product import Product


class ProductDAO:
    _SELECT = 'SELECT * FROM public."Product" ORDER BY product_id'
    _INSERT = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _DELETE = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def show_products(cls):
        with DBConnection.get_cursor() as cursor:
            cursor.execute(cls._SELECT)
            products = cursor.fetchall()
            return [Product(product[0], product[1], product[2]) for product in products]


if __name__ == '__main__':
    productos = ProductDAO.show_products()
    log.debug(productos)


