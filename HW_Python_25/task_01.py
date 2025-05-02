#Напишите функцию find_longest_word, которая будет принимать список слов и возвращать
# самое длинное слово из списка. Аннотируйте типы аргументов и возвращаемого значения функции.
from typing import List

def find_longest_word(lst: List[str]) -> str:
    return max(lst, key=len)


if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "dragonfruit"]
    result = find_longest_word(words)
    print(result)  # Ожидаемый вывод: "dragonfruit"