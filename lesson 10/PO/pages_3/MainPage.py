from selenium.webdriver.common.by import By
import allure
class MainPage:
    
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.fullscreen_window()
        self._driver.implicitly_wait(5)
    
    @allure.step("Авторизация. Вводим данные пользователя: логин")
    def authorization_user(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(data)
    
    @allure.step("Авторизация. Вводим данные пользователя: пароль")
    def authorization_password(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(data)
    
    @allure.step("Авторизация. Нажимаем Login")
    def authorization_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        
    @allure.step("Главная. Добавляем товары в корзину")
    def add_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()