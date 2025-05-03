# Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию,
# а также методы calculate_area() для вычисления площади прямоугольника и
# calculate_perimeter() для вычисления периметра прямоугольника.
# Переопределить методы __str__, __repr__.
# Затем создайте экземпляр класса Rectangle и выведите информацию о нем,
# его площадь и периметр.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник с шириной '{self.width}' и высотой '{self.height}'"

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


if __name__ == "__main__":
    rectangle = Rectangle(3, 4)
    print(rectangle)
    print(repr(rectangle))
    print("Площадь прямоугольника:",rectangle.calculate_area())
    print("Периметр прямоугольника:",rectangle.calculate_perimeter())
