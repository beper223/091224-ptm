# Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)
# Пример использования:
class Counter:
    def __init__(self,count):
        self.count = count

    def __str__(self):
        return f"{self.count}"


    def __int__(self):
        return self.count

    # ============== in-place operators ===================
    def __iadd__(self, other):
        self.count += other
        return self

    def __isub__(self, other):
        self.count -= other
        return self

counter = Counter(5)
counter += 3
print(counter)  # Вывод: 8
counter -= 2
print(int(counter))  # Вывод: 6