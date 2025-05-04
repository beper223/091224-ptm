# Напишите декоратор validate_args, который будет проверять типы аргументов функции и
# выводить сообщение об ошибке, если переданы аргументы неправильного типа. Декоратор
# должен принимать ожидаемые типы аргументов в качестве параметров.
# Пример использования:

def validate_args(*expected_types):
    def decorator(func):
        def wrapper(*args):
            for arg, expected in zip(args,expected_types):
                if not isinstance(arg,expected):
                    raise TypeError(
                        f"Аргумент '{arg}' имеет неправильный тип {type(arg)}. "
                        f"Ожидается {expected}")
            return func(*args)
        return wrapper
    return decorator

@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


greet(25, "Анна")  # Все аргументы имеют правильные типы
greet("25", "Анна")  # Возникнет исключение TypeError


# Ожидаемый вывод:
# Привет, Анна! Тебе 25 лет.
# TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.