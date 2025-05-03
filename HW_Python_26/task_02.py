# Напишите программу, которая принимает в качестве аргумента командной строки путь к
# директории и выводит список всех файлов и поддиректорий внутри этой директории. Для
# этой задачи используйте модуль os и его функцию walk. Программа должна выводить
# полный путь к каждому файлу и директории.

import sys
import os

def list_path(path_name:str) -> None:
    abs_path_name = os.path.abspath(path_name)
    if not os.path.exists(abs_path_name):
        print(f"Ошибка: путь '{abs_path_name}' не существует")
        return
    if not os.path.isdir(abs_path_name):
        print(f"Ошибка: путь '{abs_path_name}' не является директорией")
        return
    for root, dirs, files in os.walk(abs_path_name):
        for d in dirs:
            print(os.path.join(root,d))
        for f in files:
            print(os.path.join(root,f))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python task_02.py <путь_к_папке>")
    else:
        list_path(sys.argv[1])