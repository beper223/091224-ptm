import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
    driver.maximize_window()
    yield driver
    driver.quit()

def test_find_text_in_iframe(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    SEARCH_TEXT = r'semper posuere integer et senectus justo curabitur.'
    iframe_locator = (By.TAG_NAME, "iframe")
    body_locator = (By.TAG_NAME, "body")
    wait = WebDriverWait(driver, 10)

    iframes = wait.until(EC.presence_of_all_elements_located(iframe_locator))
    target_iframe = None

    for iframe in iframes:
        driver.switch_to.frame(iframe)
        body_text = driver.find_element(*body_locator).text
        if SEARCH_TEXT in body_text:
            target_iframe = iframe
            break
        driver.switch_to.default_content()

    assert target_iframe is not None, "Iframe с искомым текстом не найден"

    # код избыточен, потому что мы уже внутри нужного iframe.
    # driver.switch_to.frame(iframe)

    elements = driver.find_elements(By.XPATH, "//p")
    target_el = None
    for el in elements:
        if SEARCH_TEXT in el.text:
            #print(el.text)
            target_el = el
            break

    assert target_el is not None and target_el.is_displayed(), "Текст не отображается на странице"

def test_drag_image_to_trash(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 10)
    trash_locator = (By.ID, "trash")
    iframe_locator = (By.CSS_SELECTOR, "iframe.demo-frame")
    agree_button_locator = (By.XPATH, "//button[@aria-label='Соглашаюсь' and contains(@class, 'fc-primary-button')]")
    gallery_items_locator = (By.CSS_SELECTOR, "#gallery > li")
    trash_items_locator = (By.CSS_SELECTOR, "#trash > ul > li")

    # здесь приходится нажимать кнопку "Соглашаюсь"
    agree_button = wait.until(EC.element_to_be_clickable(agree_button_locator))
    agree_button.click()

    iframe = wait.until(EC.presence_of_element_located(iframe_locator))
    driver.switch_to.frame(iframe)

    gallery_items = driver.find_elements(*gallery_items_locator)
    draggable_li = gallery_items[0]
    trash = driver.find_element(*trash_locator)

    actions = ActionChains(driver)
    actions.drag_and_drop(draggable_li, trash).perform()

    # задержка, чтобы сработала анимация
    time.sleep(2)
    # Проверяем, что в корзине 1 изображение, а в галерее 3
    trash_items = driver.find_elements(*trash_items_locator)
    gallery_items = driver.find_elements(*gallery_items_locator)
    assert len(trash_items) == 1, f"Ожидалось 1 элемент в корзине, найдено: {len(trash_items)}"
    assert len(gallery_items) == 3, f"Ожидалось 3 элемента в галерее, найдено: {len(gallery_items)}"
