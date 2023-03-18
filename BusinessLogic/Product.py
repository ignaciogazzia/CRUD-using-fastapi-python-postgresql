from logger import log


class Product:

    def __init__(self, product_id, title, created_at):
        self._product_id = product_id
        self._title = title
        self._created_at = created_at

    def __str__(self):
        return f'ID {self._product_id} | TITLE: {self._title} | CREATED AT {self._created_at}  '

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, title):
        self.title = title

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at


if __name__ == '__main__':
    product1 = Product('1', 'Motosierra', '17/03/2023')
    log.debug(product1)

