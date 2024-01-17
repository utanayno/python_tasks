from selenium.webdriver.common.by import By
class MainPage:
    #делаем конструктор и добавляем в него драйвер
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.fullscreen_window()

    def set_time(self):
        #установить время
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("5")

    def input_numbers(self):
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click()
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click()
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()

    def get_result(self):
        txt = self._driver.find_element(By.CSS_SELECTOR,"div.screen").text
        return txt





    