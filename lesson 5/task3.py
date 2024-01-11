# сделала код для Chrome отдельно и для Firefox отдельно, попробовала объединить - не работает.
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# открыть Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
# в переменную положили строковое значение локатора
search_locator = "[onclick='addElement()']"
# нашли элемент по локатору
search_add_element = driver.find_element(By.CSS_SELECTOR, search_locator)
# нажали на элемент
search_add_element.send_keys(Keys.RETURN)
search_add_element.send_keys(Keys.RETURN)
search_add_element.send_keys(Keys.RETURN)
search_add_element.send_keys(Keys.RETURN)
search_add_element.send_keys(Keys.RETURN)

delete_button = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print(len(delete_button))

sleep(5)

#тут код для Firefox, как сделать один код для двух браузеров - я не нашла.
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# открыть Firefox
driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
# в переменную положили строковое значение локатора
search_locator = "[onclick='addElement()']"
# нашли элемент по локатору
search_add_element = driver.find_element(By.CSS_SELECTOR, search_locator)
# нажали на элемент
search_add_element.send_keys(Keys.RETURN)
search_add_element.send_keys(Keys.RETURN)
search_add_element.send_keys(Keys.RETURN)
search_add_element.send_keys(Keys.RETURN)
search_add_element.send_keys(Keys.RETURN)

delete_button = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print(len(delete_button))

sleep(5)