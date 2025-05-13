# Напишите функцию extract_emails(text), которая извлекает все адреса электронной
# почты из заданного текста и возвращает их в виде списка.
import re

def extract_emails(txt: str) -> list[str]:
    #pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    pattern = r'\b[\w.-]+@[\w.-]+\.\w{2,}\b'
    return re.findall(pattern, txt)

if __name__ == "__main__":
    text = "Contact us at info@example.com or support@example.com for assistance."
    emails = extract_emails(text)
    print(emails)  # Вывод: ['info@example.com', 'support@example.com']