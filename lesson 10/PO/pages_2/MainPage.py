from selenium.webdriver.common.by import By
import allure
class MainPage:
    
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.fullscreen_window()
    
    @allure.step("Устанавливаем время")
    def set_time(self, time : int):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time)
    
    @allure.step("Кликаем на цифры и на submit")
    def input_numbers(self):
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click()
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click()
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()
    
    @allure.step("Получаем результат вычисления")
    def get_result(self) -> str:
        txt = self._driver.find_element(By.CSS_SELECTOR,"div.screen").text
        return txt





    