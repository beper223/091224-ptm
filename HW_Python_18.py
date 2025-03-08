# Написать программу, вычисляющую факториал числа.
# Решить задачу с помощью рекурсии.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Введите число для вычисления факториала: "))
print(f"Факториал числа {number} равен {factorial(number)}")

# Напишите программу, которая использует рекурсию для вычисления суммы цифр числа.
# Создайте функцию sum_digits, которая принимает один аргумент - число, для которого нужно вычислить сумму цифр.
# Используйте условие выхода из рекурсии, когда число состоит из одной цифры. Выведите результат на экран.

def sum_digits_non_tail(n):
    if n < 10:
        return n
    return n % 10 + sum_digits_non_tail(n // 10)

def sum_digits_tail(n, accumulator=0):
    if n < 10:
        return accumulator + n
    return sum_digits_tail(n // 10, accumulator + n % 10)


a = 12345
print("Сумма цифр: ", sum_digits_non_tail(a))  # 15
print("Сумма цифр: ", sum_digits_tail(a))  # 15