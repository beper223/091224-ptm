def is_pantogram(string: str):
    i = ord('a')
    while i < ord('z') + 1:
        if chr(i) not in string.lower():
            return "не "
        i += 1
    return ""

def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = 0
    consonant_count = 0
    i = 0
    while i < len(input_string):
        if input_string[i] in vowels:
            vowel_count += 1
        if input_string[i] in consonants:
            consonant_count += 1
        i += 1
    print(f"Количество гласных букв : {vowel_count}")
    print(f"Количество согласных букв: {consonant_count}")

n = is_pantogram(input("Введите строку: "))
print(f"Строка {n}является панграммой")

count_vowels_and_consonants(input("Введите строку: "))
