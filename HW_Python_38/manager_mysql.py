"""Контекстный менеджер
"""

import mysql.connector
from local_settings import dbconfig


class MySQLConnection:
    def __init__(self, db_config):
        self.dbconfig = db_config
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.dbconfig)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        if exc_type:
            print(f"Исключение: {exc_value}")

    def show_databases(self):
        try:
            self.cursor.execute("SHOW DATABASES;")
            result = self.cursor.fetchall()
            for x in result:
                dbname = x[0]
                if '050824' in dbname:
                    print(dbname)
        except Exception as e:
            print(e)

    def show_tables(self):
        try:
            self.cursor.execute(f"USE {self.dbconfig["database"]};")
            self.cursor.execute("SHOW TABLES;")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")

    def get_fields(self, table):
        self.cursor.execute(f"DESCRIBE {table}")
        return [row[0] for row in self.cursor.fetchall()]

    def join_tables(self, tables: list, fltr=None):
        valid_tables = {'Users', 'Products', 'Sales'}
        if not set(tables).issubset(valid_tables):
            print("Ошибка: Указаны недопустимые таблицы.")
            return None
        try:
            if len(tables) == 1:
                query = f"SELECT * FROM {tables[0]}"
            elif set(tables) == {'Users', 'Sales'}:
                query = """
                    SELECT * FROM Users
                    JOIN Sales ON Users.id = Sales.id
                """
            elif set(tables) == {'Products', 'Sales'}:
                query = """
                    SELECT * FROM Products
                    JOIN Sales ON Products.pid = Sales.pid
                """
            elif set(tables) == {'Users', 'Products', 'Sales'}:
                query = """
                    SELECT * FROM Users
                    JOIN Sales ON Users.id = Sales.id
                    JOIN Products ON Products.pid = Sales.pid
                """
            else:
                print("Ошибка: Соединение для указанных таблиц не реализовано.")
                return None
            if type(fltr) == list:
                query = f"{query} {fltr[0]}"
                self.cursor.execute(query,fltr[1])
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None

    def search_by_field(self, table: str, field: str, value):
        try:
            query = f"SELECT * FROM {table} WHERE {field} = %s"
            self.cursor.execute(query, (value,))
            return self.cursor.fetchall()
        except Exception as e:
            return f"Ошибка при выполнении запроса: {e}"

if __name__ == "__main__":
    with MySQLConnection(dbconfig) as db_manager:
        db_manager.show_databases()
        db_manager.show_tables("050824_BAR_sakila")

