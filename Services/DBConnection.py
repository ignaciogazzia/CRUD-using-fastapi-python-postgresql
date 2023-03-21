import sys

from logger import log
import psycopg2 as bd


class DBConnection:
    _DATABASE = 'Personas'
    _USERNAME = 'postgres'
    _PASSWORD = 'igna+1234'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _connection = None
    _cursor = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            try:
                cls._connection = bd.connect(
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Connected successfully to DB: {cls._connection}')
                return cls._connection
            except Exception as e:
                log.error(f'Ocurrio excepcion {e}')
                sys.exit()  # Termina nuestro programa...
        else:
            return cls._connection

    @classmethod
    def get_cursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.get_connection().cursor()
                log.debug(f'Cursor opened correctly {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Exception obtaining cursor {e}')
                sys.exit()
        else:
            return cls._cursor

    @property
    def connection(self):
        return self._connection

    @classmethod
    def commit(cls):
        cls._connection.commit()

if __name__ == "__main__":
    DBConnection.get_connection()
    DBConnection.get_cursor()
