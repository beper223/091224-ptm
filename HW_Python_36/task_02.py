# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и
# уровень заголовков, а затем использует библиотеку Beautiful Soup для парсинга HTML и
# извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом.

import requests
from bs4 import BeautifulSoup
from typing import List

def get_tags(url: str,level: str) -> List[str]:
    # if not level.isdigit() or not (1 <= int(level) <= 6):
    #     print("Уровень заголовка должен быть числом от 1 до 6.")
    #     return []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all(f'h{level}')
    unique_tags = set()
    for tag in tags:
        text = tag.get_text(strip=True)
        if text:
            unique_tags.add(text)
    return sorted(unique_tags)

if __name__ == "__main__":
    # URL = input("Введите URL-адрес веб-страницы: ")
    # LEVEL = input("Введите уровень заголовка: ")
    URL = "https://it4each.com"
    LEVEL = "2"
    tags = get_tags(URL,LEVEL)
    if tags:
        print(f"Заголовки уровня h{LEVEL} страницы {URL} :")
        for i, tag in enumerate(tags, 1):
            print(f"{i}. {tag}")
    else:
        print(f"Заголовки уровня h{LEVEL} на странице {URL} не найдены.")

