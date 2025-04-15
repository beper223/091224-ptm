# Напишите программу, которая принимает список чисел от пользователя и использует функцию reduce из модуля functools,
# чтобы найти произведение всех чисел в списке. Затем программа должна использовать функцию itertools.accumulate
# для накопления произведений чисел в новом списке.
# В результате программа должна вывести список, содержащий накопленные произведения.

from functools import reduce
from itertools import accumulate
from operator import mul

def product_and_accumulate(words: list[str]) -> tuple:
    numbers = [int(x) for x in words]
    # product_red = reduce(lambda x, y: x * y, numbers)
    # product_accum =  list(accumulate(numbers,lambda x, y: x * y))
    # mul короче и читабельнее lambda, особенно когда ты просто умножаешь.
    # немного быстрее, потому что это встроенная функция, не анонимная lambda.
    product_red = reduce(mul, numbers) # перемножает все числа в списке
    product_accum = list(accumulate(numbers, mul)) # возвращает список, где каждый элемент — это произведение всех предыдущих чисел.
    return product_red, product_accum


if __name__ == "__main__":
    user_input = input("Введите список чисел: ").split()
    result = product_and_accumulate(user_input)
    print(*result,sep="\n")