# Напишите программу, которая принимает в качестве аргумента командной строки путь к
# файлу .py и запускает его. При запуске файла программа должна выводить сообщение
# "Файл <имя файла> успешно запущен". Если файл не существует или не может быть
# запущен, программа должна вывести соответствующее сообщение об ошибке.

import sys
import os
import subprocess

def run_python_file(file_name:str) -> None:
    if not os.path.exists(file_name):
        print(f"Ошибка: путь '{file_name}' не существует")
        return
    if not os.path.isfile(file_name):
        print(f"Ошибка: путь '{file_name}' не является файлом")
        return
    if not file_name.endswith('.py'):
        print(f"Ошибка: файл '{file_name}' не является python-файлом")
        return
    try:
        subprocess.run(['python',file_name],check=True)
        print(f"Файл '{file_name}' успешно запущен")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении файла: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python task_01.py <путь_к_файлу.py>")
    else:
        run_python_file(sys.argv[1])