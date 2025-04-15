# Напишите программу, которая принимает список слов от пользователя и использует генераторное выражение (comprehension)
# для создания нового списка, содержащего только те слова, которые начинаются с гласной буквы.
# Затем программа должна использовать функцию map, чтобы преобразовать каждое слово в верхний регистр.
# В результате программа должна вывести новый список, содержащий только слова, начинающиеся с гласной буквы
# и записанные в верхнем регистре.

def filter_and_upper_words(words: list[str]) -> list[str]:
    vowels = 'aeiouаеёиоуыэюя'
    vowel_words = [word for word in words if word[0].lower() in vowels]
    return list(map(lambda x: x.upper(), vowel_words))


if __name__ == "__main__":
    user_input = input("Enter words separated by spaces: ").split()
    result = filter_and_upper_words(user_input)
    print("Result:", result)