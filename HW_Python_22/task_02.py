# Напишите программу, которая открывает файл, считывает его содержимое и выполняет операции над числами в файле. Обработайте возможные исключения при открытии файла (FileNotFoundError) и при выполнении операций над числами (ValueError, ZeroDivisionError). Используйте конструкцию try-except-finally для обработки исключений и закрытия файла в блоке finally.

def process_numbers_from_file(filename):
    # для безопасного использования блока finally
    file = None
    try:
        file = open(filename, encoding='utf-8')
        lines = file.readlines()

        if len(lines) < 2:
            raise ValueError("файл должен содержать как минимум две строки с числами.")

        num1 = float(lines[0].strip())
        num2 = float(lines[1].strip())

        result = num1 / num2
        print(f"Результат деления: {result}")

    except FileNotFoundError:
        print(f'Ошибка: файл "{filename}" не найден')
    # ValueError: Тип аргумента правильный, но значение недопустимо
    # TypeError: Тип аргумента вообще не тот, с ним нельзя работать
    except TypeError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except ZeroDivisionError:
        print("Произошла ошибка: деление на ноль.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    process_numbers_from_file("numbers.txt")