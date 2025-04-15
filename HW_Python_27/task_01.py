# Напишите функцию, которая принимает на вход список чисел и возвращает сумму
# квадратов только четных чисел из списка, используя функциональные подходы
# (например, map, filter и reduce).

from functools import reduce

def sum_even_squares(nums: list[str]) -> int:
    numbers = map(int, nums)
    #print(list(numbers))
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    squares_numbers = map(lambda x: x ** 2, even_numbers)
    return reduce(lambda x, y: x + y, squares_numbers) # sum(numbers)


if __name__ == "__main__":
    user_input = input("Введите список чисел: ").split()
    result = sum_even_squares(user_input)
    print(result)

