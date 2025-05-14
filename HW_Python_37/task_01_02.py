# В базе данных MySQL три таблицы. Users с полями (id, name, age), Products с полями
# (pid, prod, quantity) и Sales с полями (sid, id, pid).
# 1. Программа должна запросить у пользователя название таблицы и вывести все ее строки или
# сообщение, что такой таблицы нет.
# 2. Программа должна вывести все имена из таблицы users, дать пользователю выбрать одно
# из них и вывести все покупки этого пользователя.

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

    def show_table(self, table: str):
        valid_tables = {'Users', 'Products', 'Sales'}
        if table not in valid_tables:
            print("Ошибка: Указана недопустимая таблица.")
            return None
        try:
            query = f"SELECT * FROM {table}"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None

    def get_user_names(self):
        try:
            self.cursor.execute("SELECT name FROM Users")
            return [row[0] for row in self.cursor.fetchall()]
        except Exception as e:
            print(f"Ошибка при получении имен: {e}")
            return []

    def search_by_username(self, value):
        try:
            query = """
                SELECT Products.prod, Products.quantity
                FROM Users
                JOIN Sales ON Users.id = Sales.id
                JOIN Products ON Products.pid = Sales.pid
                WHERE Users.name = %s
            """
            self.cursor.execute(query, (value,))
            return self.cursor.fetchall()
        except Exception as e:
            return f"Ошибка при выполнении запроса: {e}"

if __name__ == "__main__":
    with MySQLConnection(dbconfig) as db_manager:
        table_name = input("Введите название таблицы (Users, Products, Sales): ")
        rows = db_manager.show_table(table_name)
        columns = [desc[0] for desc in db_manager.cursor.description]
        if not rows:
            print("Таблица не найдена или пуста.")
            exit()
        print(f"Содержимое таблицы {table_name}:")
        for row in rows:
            print(dict(zip(columns, row)))

        names = db_manager.get_user_names()
        print("Доступные пользователи:")
        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")
        choice = input("Выберите имя пользователя: ")
        if choice in names:
            purchases = db_manager.search_by_username(choice)
            if purchases:
                print(f"Покупки пользователя {choice}:")
                for prod, qty in purchases:
                    print(f"{prod} (кол-во: {qty})")
            else:
                print("У пользователя нет покупок.")
        else:
            print("Некорректный выбор пользователя.")