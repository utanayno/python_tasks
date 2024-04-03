from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from pages_2.MainPage import MainPage

@allure.title("Проверка результата вычисления калькулятора")
@allure.description("Проверить, что результат вычисления калькулятора равен ожидаемому. Результат должен показаться через 5 секунд")
@allure.feature("READ")
@allure.severity("critical")
def test_calc():
    browser = webdriver.Chrome(service=ChromeService((ChromeDriverManager().install())))
    main_page = MainPage(browser)
    #sleep(4)
    main_page.set_time("5")
    main_page.input_numbers()
    expected_result = "15"
    waiter = WebDriverWait(browser, 6) # Драйвер ждет 6 секунд
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), expected_result)
    ) 
    
    result = main_page.get_result()
    with allure.step("Проверить, что результат вычисления равен 15"):
        assert result == expected_result
    browser.quit()