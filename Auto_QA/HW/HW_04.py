import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    service = Service(r'c:\dist\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_button_text_change(driver):
    driver.get("http://uitestingplayground.com/textinput")
    button_locator = (By.ID, "updatingButton")
    input_locator = (By.ID, "newButtonName")
    wait = WebDriverWait(driver, 10)

    input_field = driver.find_element(*input_locator)
    input_field.clear()
    input_field.send_keys("ITCH")

    button = driver.find_element(*button_locator)
    button.click()
    wait.until(EC.text_to_be_present_in_element(button_locator, "ITCH"))

    # updated_text = button.text
    # assert updated_text == "ITCH", f"Ожидался текст кнопки 'ITCH', но был '{updated_text}'"

def test_third_image_alt(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait = WebDriverWait(driver, 15)
    container_locator = (By.CSS_SELECTOR, "#image-container img")
    text_locator = (By.ID, "text")

    wait.until(EC.text_to_be_present_in_element(text_locator, "Done!"))

    images = driver.find_elements(*container_locator)
    assert len(images) >= 3, f"Ожидалось минимум 3 изображения, но найдено {len(images)}"

    third_img_alt = images[2].get_attribute("alt")
    assert third_img_alt == "award", f"Ожидался alt='award', но получен alt='{third_img_alt}'"
