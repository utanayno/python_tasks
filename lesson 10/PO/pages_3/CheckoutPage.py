from selenium.webdriver.common.by import By
import allure

class CheckoutPage:
    
    def __init__(self, driver):
        self._driver = driver
    
    @allure.step("Checkout. Вводим имя")   
    def fill_checkout_name(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(data)
    
    @allure.step("Checkout. Вводим фамилию")
    def fill_checkout_lastname(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(data)

    @allure.step("Checkout. Вводим почтовый индекс")
    def fill_checkout_postalcode(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(data)
    
    @allure.step("Checkout. Нажимаем 'Continue'")
    def checkout_continue(self):       
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
    
    @allure.step("Получаем итоговую сумму покупки (Total)")
    def get_total(self) -> str:
        txt = self._driver.find_element(By.CSS_SELECTOR,"#checkout_summary_container > div > div.summary_info > div.summary_info_label.summary_total_label").text
        return txt