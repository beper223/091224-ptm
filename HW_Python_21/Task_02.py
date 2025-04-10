# Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке, включающий поля name, age и city. Создайте список объектов Person и выведите информацию о каждом человеке на экран.
#
# Пример вывода:
# Name: Alice, Age: 25, City: New York
# Name: Bob, Age: 30, City: London
# Name: Carol, Age: 35, City: Paris

from collections import namedtuple

if __name__ == "__main__":

    Person = namedtuple('Person', ['name', 'age', 'city'])
    Persons = [
        Person('Alice', 25, 'New York'),
        Person('Bob', 30, 'London'),
        Person('Carol', 35, 'Paris')
    ]

    for person in Persons:
        print(f"Name: {person.name}, Age: {person.age}, City: {person.city}")

