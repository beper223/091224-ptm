# Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
# Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
# Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.

def anagrams(lst: list):
    anagram_group = []
    words = []
    for word in lst:
        if word in words:
            continue
        new_list = [word]
        for i in range(lst.index(word) + 1, len(lst)):
            #if set(lst[i]) == set(word):
            if sorted(lst[i]) == sorted(word):
                new_list.append(lst[i])
                words.append(lst[i])
        if len(new_list) > 1:
            anagram_group.append(new_list)
    return anagram_group

#print('Анаграммы: ',*anagrams(['cat', 'dog', 'tac', 'god', 'act', 'gsadfas', 'gsadfsa']),sep='')

# Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет, является ли set1 подмножеством set2.
# Функция должна возвращать True, если все элементы из set1 содержатся в set2, и False в противном случае.
# Функция должна быть реализована без использования встроенных методов issubset или <=.

def is_subset(set1: set, set2: set) -> bool:
    for item in set1:
        if item not in set2:
            return False
    return True

print(is_subset({1, 2, 3},{1, 2, 3, 4, 5}))