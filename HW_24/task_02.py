# Напишите генератор, который будет генерировать арифметическую прогрессию

def arithmetic_progression(start, step):
    current = start
    while True:
        yield current  # Отправляем текущее значение
        current += step


gen = arithmetic_progression(1, 2)

print(next(gen))
print(next(gen))
print(next(gen))

