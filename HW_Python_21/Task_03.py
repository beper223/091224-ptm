# Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает значение для указанного ключа с использованием метода get или setdefault. Создайте функцию get_value_from_dict, которая принимает словарь и ключ в качестве аргументов, и возвращает значение для указанного ключа, используя метод get или setdefault в зависимости от выбранного варианта. Выведите полученное значение на экран.
#
# Пример словаря:
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
#
# Пример вывода:
# Введите ключ для поиска: banana
# Использовать метод get (y/n)? y
# Значение для ключа 'banana': 6

def get_value_from_dict(dct: dict, key: str, is_get: str) -> int:
    if is_get == 'y':
        return dct.get(key)
    else:
        return dct.setdefault(key, 0)

if __name__ == "__main__":
    my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
    my_key = input("Введите ключ для поиска: ")
    my_is_get = input("Использовать метод get (y/n)? ")
    print(f"Значение для ключа '{my_key}': {get_value_from_dict(my_dict, my_key, my_is_get)}")
