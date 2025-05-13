# Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и
# возвращает список наиболее часто встречающихся слов на веб-страницах. Для каждого
# URL-адреса функция должна получить содержимое страницы с помощью запроса GET и
# использовать регулярные выражения для извлечения слов. Затем функция должна
# подсчитать количество вхождений каждого слова и вернуть наиболее часто встречающиеся
# слова в порядке убывания частоты.

import requests
import re
from collections import Counter
from bs4 import BeautifulSoup


def find_common_words(url_list):
    word_counter = Counter()
    for url in url_list:
        try:
            response = requests.get(url)

            soup = BeautifulSoup(response.text, "html.parser")
            # <script> содержит JavaScript-код, который не нужен при анализе текста.
            # <style> содержит CSS-стили, которые тоже не являются полезным содержимым страницы.
            for tag in soup(["script", "style"]):
                tag.extract()
            text = soup.get_text(separator=' ')
            #print(text)

            words = re.findall(r'\b[a-zA-Z]+\b', text)
            word_counter.update(words)
        except requests.RequestException as e:
            print(f"Ошибка при обработке {url}: {e}")
    return word_counter.most_common()

if __name__ == "__main__":
    urls = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://www.python.org"
    ]

    common_words = find_common_words(urls)
    print("топ-10 слов:")
    for word, count in common_words[:10]:
        print(f"{word}: {count}")