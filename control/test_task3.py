from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_total():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #перейти на сайт
    driver.get('https://www.saucedemo.com/')
    #авторизация
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    driver.implicitly_wait(5)
    #добавление в корзину
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    #переход в корзину
    driver.get('https://www.saucedemo.com/cart.html')
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    driver.implicitly_wait(5)
    #заполнение формы
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Julia")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Tanayno")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("3029AD")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    #сравнение суммы покупки
    txt = driver.find_element(By.CSS_SELECTOR,"#checkout_summary_container > div > div.summary_info > div.summary_info_label.summary_total_label").text
    assert txt == "Total: $58.29"
    driver.quit()    