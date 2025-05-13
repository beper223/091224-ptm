# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod,
# quantity) и Sales с полями (sid, id, pid). Написать мини-интерфейс к базе данных, который умеет
# выполнять разные команды.
# 1. Выбрать таблицу для запроса. Предусмотреть возможность выбрать несколько таблиц.
# Вывести результат их соединения, если это возможно, или сообщение об ошибке.
# 2. Выбрать одно поле из выбранной таблицы и искомое значение этого поля. Вывести все
# подходящие строки
# 3. Ввести список полей выбранной таблицы.
# 4. При вводе искомого значения добавить возможность выбора знака - найти записи, в
# которых выбранное поле больше, меньше или равно введенному значению.


from manager_mysql import MySQLConnection
from local_settings import dbconfig


if __name__ == "__main__":

    with MySQLConnection(dbconfig) as db_manager:
        result = db_manager.show_tables()
        print(f"Таблицы базы {dbconfig["database"]}: \n" + ", ".join(item[0] for item in result))

    print("Доступные таблицы: Users, Products, Sales")
    tables = input("Введите названия таблиц через запятую: ").replace(" ", "").split(",")
    with MySQLConnection(dbconfig) as db_manager:
        result = db_manager.join_tables(tables)
        if result is None:
            exit()
        columns = [desc[0] for desc in db_manager.cursor.description]
        print("\nРезультат запроса:")
        for row in result:
            print(dict(zip(columns, row)))

        all_fields = {}
        for table in tables:
            for field in db_manager.get_fields(table):
                all_fields[f"{table}.{field}"] = field

        #print("\n1. 🔍 Фильтрация по полю")
        print("Доступные поля для поиска:")
        for i, full_field in enumerate(all_fields, 1):
            print(f"{i}. {full_field}")

        field_num = int(input("Выберите номер поля для фильтрации: "))
        selected_full_field = list(all_fields.keys())[field_num - 1]
        selected_table, selected_field = selected_full_field.split(".")
        operator = input("Введите оператор сравнения (=, >, <): ")
        value = input("Введите значение для поиска: ")
        filtered_query = f" WHERE {selected_table}.{selected_field} {operator} %s"
        result = db_manager.join_tables(tables,[filtered_query,(value,)])
        if result is None:
            exit()
        columns = [desc[0] for desc in db_manager.cursor.description]
        print("\nРезультат запроса:")
        for row in result:
            print(dict(zip(columns, row)))
        # Users, Products, Sales
