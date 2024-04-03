from selenium.webdriver.common.by import By
import allure

class MainPage:
    
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.fullscreen_window()

    @allure.step("Вводим имя {data}")
    def fill_first_name(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(data)

    @allure.step("Вводим фамилию {data}")
    def fill_last_name(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(data)

    @allure.step("Вводим адрес {data}")
    def fill_address(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(data)

    @allure.step("Вводим эл. почту {data}")
    def fill_email(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(data)
    
    @allure.step("Вводим телефон {data}")    
    def fill_phone(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(data)
    
    @allure.step("Вводим город {data}")
    def fill_city(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(data)
    
    @allure.step("Вводим страну {data}")
    def fill_country(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(data)

    @allure.step("Вводим позицию {data}")
    def fill_position(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(data)
    
    @allure.step("Вводим компанию {data}")
    def fill_company(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(data)
    
    @allure.step("Вводим почтовый индекс {data}")
    def fill_zip(self, data : str):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(data)
    
    @allure.step("Нажимаем submit")
    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()
    
    @allure.step("Получаем цвет поля с почтовым индексом")    
    def color_zip(self) -> str:
        as_is_zip = self._driver.find_element(By.CSS_SELECTOR, "div#zip-code").value_of_css_property("background-color")
        return as_is_zip
    
    @allure.step("Получаем цвет поля с именем") 
    def color_firstname(self) -> str:
        as_is_color_firstname = self._driver.find_element(By.CSS_SELECTOR, "div#first-name").value_of_css_property("background-color")
        return as_is_color_firstname
    
    @allure.step("Получаем цвет поля с фамилией") 
    def color_lastname(self) -> str:
        as_is_color_lastname = self._driver.find_element(By.CSS_SELECTOR, "div#last-name").value_of_css_property("background-color")
        return as_is_color_lastname
    
    @allure.step("Получаем цвет поля с адресом") 
    def color_address(self) -> str:
        as_is_color_address = self._driver.find_element(By.CSS_SELECTOR, "div#address").value_of_css_property("background-color")
        return as_is_color_address
    
    @allure.step("Получаем цвет поля с эл. почтой")
    def color_email(self) -> str:
        as_is_color_email = self._driver.find_element(By.CSS_SELECTOR, "div#e-mail").value_of_css_property("background-color")
        return as_is_color_email
    
    @allure.step("Получаем цвет поля с телефоном")
    def color_phone(self) -> str:
        as_is_color_phone = self._driver.find_element(By.CSS_SELECTOR, "div#phone").value_of_css_property("background-color")
        return as_is_color_phone
    
    @allure.step("Получаем цвет поля с городом")
    def color_city(self) -> str:
        as_is_color_city = self._driver.find_element(By.CSS_SELECTOR, "div#city").value_of_css_property("background-color")
        return as_is_color_city
    
    @allure.step("Получаем цвет поля со страной")
    def color_country(self) -> str:
        as_is_color_country = self._driver.find_element(By.CSS_SELECTOR, "div#country").value_of_css_property("background-color")
        return as_is_color_country
    
    @allure.step("Получаем цвет поля с позицией")
    def color_jobposition(self) -> str:
        as_is_color_jobposition = self._driver.find_element(By.CSS_SELECTOR, "div#job-position").value_of_css_property("background-color")
        return as_is_color_jobposition
    
    @allure.step("Получаем цвет поля с компанией")
    def color_company(self) -> str:
        as_is_color_company = self._driver.find_element(By.CSS_SELECTOR, "div#company").value_of_css_property("background-color")
        return as_is_color_company  