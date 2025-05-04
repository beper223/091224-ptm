# Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов
# функции в лог-файл. Каждый вызов функции должен быть записан на новой строке в
# формате "Аргументы: <аргументы>, Результат: <результат>". Используйте модуль logging
# для записи в лог-файл.

import logging

# Настройка логирования
logging.basicConfig(
    filename='log.txt',
    encoding='utf-8',
    level=logging.INFO,
    format='%(message)s'  # Только сообщение, без времени и уровня
)

def log_args(func):
    def wrapper(*args):
        result = func(*args)
        args_str = ", ".join(map(str,args))
        logging.info(f'Аргументы: {args_str}, Результат: {result}')
        return result
    return wrapper

@log_args
def add(a, b):
    return a + b


add(2, 3)
add(5, 7)

# Ожидаемый вывод в файле log.txt:
# Аргументы: 2, 3, Результат: 5
# Аргументы: 5, 7, Результат: 12
#
# Убедитесь, что перед запуском кода у вас создан файл log.txt в той же директории, где находится скрипт Python.