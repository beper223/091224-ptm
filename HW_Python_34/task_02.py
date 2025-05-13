# Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения
# заданных ключевых слов в тексте, окружая их символами *. Функция должна быть
# регистронезависимой при поиске ключевых слов.

import re

def highlight_keywords(text: str, keywords: list[str]):
    pattern = r'\b(' + '|'.join(re.escape(word) for word in keywords) + r')\b'

    def replacer(match):
        return f'*{match.group(0)}*'

    highlighted = re.sub(pattern, replacer, text, flags=re.IGNORECASE)
    return highlighted

if __name__ == "__main__":
    text = "This is a sample text. We need to highlight Python and programming."
    keywords = ["python", "programming"]
    highlighted_text = highlight_keywords(text, keywords)
    print(highlighted_text)

# Вывод: "This is a sample text. We need to highlight *Python* and *programming*."