import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    service = Service(r'c:\dist\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_itcareerhub_main_page(driver):
    url = "https://itcareerhub.de/ru"
    driver.get(url)
    driver.implicitly_wait(2)

    # Логитип ITCareerHub
    assert driver.find_element(By.CSS_SELECTOR, 'img[alt="IT Career Hub"]'), "Логотип не найден"

    # Ссылки: “Программы”, “Способы оплаты”, “Новости”, “О нас”, “Отзывы”
    nav_links_text = ["Программы", "Способы оплаты", "Новости", "О нас", "Отзывы"]
    for text in nav_links_text:
        assert driver.find_element(By.LINK_TEXT, text), f"Ссылка '{text}' не найдена"

    # Кнопки переключения языка (ru и de)
    lang_de = driver.find_element(By.LINK_TEXT, "de")
    lang_ru = driver.find_element(By.LINK_TEXT, "ru")
    assert lang_de.is_displayed(), "Кнопка 'de' не отображается"
    assert lang_ru.is_displayed(), "Кнопка 'ru' не отображается"

    # Кликнуть по иконке с телефонной трубкой
    phone_icon = driver.find_element(By.CSS_SELECTOR, 'img[imgfield="tn_img_1710153310161"]')
    phone_icon.click()
    driver.implicitly_wait(2)

    # Проверить что текст “Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами” отображается.
    expected_text = "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"
    assert expected_text in driver.page_source, "Ожидаемый текст не найден после клика по телефону"
