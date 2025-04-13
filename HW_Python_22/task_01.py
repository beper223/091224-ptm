# Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления. Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным". Обработайте исключение и выведите соответствующее сообщение.

# class IncorrectNumberOfElements(Exception):
#     pass

if __name__ == "__main__":
    try:
        with open('./numbers.txt', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) < 2:
                raise ValueError("Файл должен содержать два числа.")
            num1 = float(lines[0].strip())
            num2 = float(lines[1].strip())
            if num1 < 0 or num2 < 0:
                raise ValueError("Число должно быть положительным.")
            result = num1 / num2
            print(f"Результат деления: {result}")
    except ZeroDivisionError:
        print("Произошла ошибка: Деление на ноль.")
    except Exception as e:
        # Обработка других исключений
        print("Произошла ошибка:", e)

