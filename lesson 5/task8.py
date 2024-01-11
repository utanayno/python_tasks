from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# открыть Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://the-internet.herokuapp.com/login')
# в переменную положили строковое значение локатора
username = "#username"
password = "#password"
login = ".fa-sign-in"
# нашли элемент по локатору
search_input_name = driver.find_element(By.CSS_SELECTOR, username)
# ввели данные
search_input_name.send_keys("tomsmith")
search_input_password = driver.find_element(By.CSS_SELECTOR, password)
search_input_password.send_keys("SuperSecretPassword!")
search_input_login = driver.find_element(By.CSS_SELECTOR, login)
search_input_login.click()

sleep(5)


# открыть Firefox
driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/login')
# в переменную положили строковое значение локатора
username = "#username"
password = "#password"
login = ".fa-sign-in"
# нашли элемент по локатору
search_input_name = driver.find_element(By.CSS_SELECTOR, username)
# ввели данные
search_input_name.send_keys("tomsmith")
search_input_password = driver.find_element(By.CSS_SELECTOR, password)
search_input_password.send_keys("SuperSecretPassword!")
search_input_login = driver.find_element(By.CSS_SELECTOR, login)
search_input_login.click()
sleep(5)