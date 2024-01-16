from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc():
    browser = webdriver.Chrome(service=ChromeService((ChromeDriverManager().install())))
    #перейти на сайт
    browser.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    browser.fullscreen_window()
    
    #в поле ввода по локатору #delay введите значение 45
    browser.find_element(By.CSS_SELECTOR, "#delay").clear()
    browser.find_element(By.CSS_SELECTOR, "#delay").send_keys("5")
    
    #ввести выражение
    sleep(4)
    browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
    browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click()
    browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click()
    browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()
    sleep(6)
    #browser.implicitly_wait(6) - не сработало, а со sleep работает (не пойму, почему)
    #проверить, что результат равен 15
    txt = browser.find_element(By.CSS_SELECTOR,"div.screen").text
    assert txt == "15"
    browser.quit()
    


    
    
    