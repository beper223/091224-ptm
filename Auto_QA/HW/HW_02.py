# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime

#service = Service("c:\\dist\\chromedriver-win64\\chromedriver.exe")
service = Service("c:\\dist\\geckodriver.exe")
options = Options()
driver = webdriver.Firefox(service=service, options=options)
driver.get("https://itcareerhub.de/ru")
sleep(3)
about_link = driver.find_element(By.LINK_TEXT, "Новости")
about_link.click()
sleep(3)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
driver.save_screenshot(f"./itcareerhub_screenshot_{timestamp}.png")
driver.quit()
