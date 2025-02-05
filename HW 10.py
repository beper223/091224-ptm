# 1. Напишите программу, которая запрашивает у пользователя строку и преобразует ее,
# удаляя все гласные буквы из строки. Используйте метод replace() для замены гласных букв на пустую строку.
# Выведите преобразованную строку на экран с помощью команды print.
def fun1():
    input_text = input(f"Введите строку: \n")
    vowels = "aeiouyAEIOUY"
    i = 0
    while i < len(vowels):
        input_text = input_text.replace(vowels[i],'')
        i += 1
    print(input_text)

# 2. Напишите программу, которая запрашивает у пользователя строку и
# определяет, содержит ли она только уникальные символы. Если все
# символы в строке уникальны, выведите соответствующее сообщение
# на экран. В противном случае выведите сообщение о том, какие
# символы повторяются. Не используйте множества и подобные
# структуры данных, которые мы пока не изучали, для проверки
# уникальности символов.

def fun2():
    seen = []
    repeated_chars = []
    input_text = input(f"Введите строку: \n")
    i = 0
    while i < len(input_text):
        if input_text[i] in seen:
            if not (input_text[i] in repeated_chars):
                repeated_chars.append(input_text[i])
        else:
            seen.append(input_text[i])
        i += 1
    if len(repeated_chars) == 0:
        print("Символы в строке уникальны.")
    else:
        i = 0
        while i < len(repeated_chars):
            repeated_chars[i] = "'" + repeated_chars[i] + "'"
            i += 1
        print(f"Символы {", ".join(repeated_chars)} повторяются.")

# 3. Напишите программу, которая запрашивает у пользователя строку и
# выравнивает ее по центру с заданной шириной. Если строка не может
# быть выровнена по центру из-за нечетной ширины, она должна быть
# выровнена смещением вправо. Используйте методы center() и rjust()
# для выравнивания строки.
def fun3():
    user_input = input("Введите строку: \n")
    width = int(input("Введите ширину: \n"))
    difference = width - len(user_input)
    if difference % 2 != 0:
        user_input = user_input.rjust(len(user_input) + 1, "+")
    centered_string = user_input.center(width,"+")
    print(f"|{centered_string}|")

# fun1()
# fun2()
# fun3()





