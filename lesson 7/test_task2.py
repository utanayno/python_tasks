from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages_2.MainPage import MainPage

def test_calc():
    browser = webdriver.Chrome(service=ChromeService((ChromeDriverManager().install())))
    #создаем экз. класса
    main_page = MainPage(browser)
    sleep(4)
    main_page.set_time()
    main_page.input_numbers()
    sleep(6)
    #проверить, что результат равен 15
    result = main_page.get_result()
    assert result == "15"
    browser.quit()