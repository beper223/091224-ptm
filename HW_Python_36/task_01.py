# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
# использует библиотеку Beautiful Soup для парсинга HTML и выводит список всех ссылок
# на странице.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List

# Функция get_urls:
# загружает страницу по URL;
# исключает мусорные ссылки (tel:, mailto:, javascript:, #);
# делает относительные ссылки абсолютными с помощью urljoin;
# убирает дубликаты с помощью set;
# возвращает отсортированный список href.
def get_urls(url: str) -> List[str]:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    unique_urls = set()
    for link in links:
        href = link.get("href")
        if not href:
            continue
        if href.startswith(("tel:", "mailto:", "javascript:", "#")):
            continue
        href = href.strip()
        full_url = urljoin(url, href)
        unique_urls.add(full_url)

    return sorted(unique_urls)

if __name__ == "__main__":
    URL = "https://it4each.com"
    hrefs = get_urls(URL)
    for href in hrefs:
        print(href)
