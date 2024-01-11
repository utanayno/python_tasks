from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# открыть Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://the-internet.herokuapp.com/entry_ad')
# в переменную положили строковое значение локатора
search_locator = "div.modal-footer"
# ждем пока откроется модальное окно
driver.implicitly_wait(10)
# нашли элемент по локатору
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
# нажали на элемент
search_input.click()
sleep(5)

# открыть Firefox
driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/entry_ad')
# в переменную положили строковое значение локатора
search_locator = "div.modal-footer"
# нашли элемент по локатору
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
# ждем пока откроется модальное окно
driver.implicitly_wait(10)
# нажали на элемент
#search_input.click()
ActionChains(driver).move_to_element(search_input).click(search_input).perform()
sleep(5)
