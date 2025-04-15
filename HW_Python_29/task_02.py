#Создайте класс Student для представления студента. Класс должен иметь атрибуты name (имя) и age (возраст), а также метод display_info(), который выводит информацию о студенте. Затем создайте экземпляр класса Student с заданным именем и возрастом и вызовите метод display_info().

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f'Name: {self.name}, age: {self.age}'

student = Student('Anton', 25)
print("Student:",student.display_info())