from selenium.webdriver.common.by import By
class MainPage:
    #делаем конструктор и добавляем в него драйвер
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.fullscreen_window()

    def authorization(self):
        #авторизация
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def add_to_cart(self):
        #добавление в корзину
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()