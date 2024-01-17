from selenium.webdriver.common.by import By
class CartPage:
    #делаем конструктор и добавляем в него драйвер
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.fullscreen_window()

    def click_checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()