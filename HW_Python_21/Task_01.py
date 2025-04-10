# Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и выводит на экран наиболее часто встречающиеся слова. Для решения задачи используйте класс Counter из модуля collections. Создайте функцию count_words, которая принимает текст в качестве аргумента и возвращает словарь с количеством вхождений каждого слова. Выведите наиболее часто встречающиеся слова и их количество.
# Пример вывода:
# Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
# sed: 2
# Lorem: 1

from collections import Counter

def clean_word(my_word: str) -> str:
    return ''.join(char.lower() for char in my_word if char.isalpha())

def count_words(text: str) -> Counter:
    return Counter([clean_word(word) for word in text.split()])


if __name__ == "__main__":
    my_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.'
    # print(count_words(my_text).most_common(10))
    for word, count in count_words(my_text).most_common(2):
        print(f"{word}: {count}")