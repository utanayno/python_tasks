from selenium.webdriver.common.by import By
import allure

class CartPage:
    
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.fullscreen_window()
        self._driver.implicitly_wait(5)
    
    @allure.step("Корзина. Нажимаем 'Checkout'")
    def click_checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()