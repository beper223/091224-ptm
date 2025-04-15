# # Напишите функцию, которая принимает на вход список функций и значение, а затем
# применяет композицию этих функций к значению, возвращая конечный результат.
from functools import reduce


def compose_functions(functions: list,value:int) -> int:
    # res - аккумулятор, начальное значение: value
    return reduce(lambda res, func: func(res), functions, value)


add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3
my_functions = [add_one, double, subtract_three]

print(compose_functions(my_functions, 5)) #должно вывести 9

