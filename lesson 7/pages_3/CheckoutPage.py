from selenium.webdriver.common.by import By
class CheckoutPage:
    #делаем конструктор и добавляем в него драйвер
    def __init__(self, driver):
        self._driver = driver
        
    def fill_checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Julia")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Tanayno")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("3029AD")
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_total(self):
        txt = self._driver.find_element(By.CSS_SELECTOR,"#checkout_summary_container > div > div.summary_info > div.summary_info_label.summary_total_label").text
        return txt