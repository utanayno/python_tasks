from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# открыть Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/classattr')
# в переменную положили строковое значение локатора
search_locator = ".btn-primary.btn-test"
# нашли элемент по локатору
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
# нажали на элемент
search_input.send_keys(Keys.RETURN)

sleep(5)

# открыть Firefox
driver = webdriver.Firefox()
driver.get('http://uitestingplayground.com/classattr')
# в переменную положили строковое значение локатора
search_locator = ".btn-primary.btn-test"
# нашли элемент по локатору
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
# нажали на элемент
search_input.send_keys(Keys.RETURN)

sleep(5)
