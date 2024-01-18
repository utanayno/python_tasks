from selenium.webdriver.common.by import By
class MainPage:
    #делаем конструктор и добавляем в него драйвер
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.fullscreen_window()

    def fill_first_name(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(data)

    def fill_last_name(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(data)

    def fill_address(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(data)

    def fill_email(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(data)
        
    def fill_phone(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(data)

    def fill_city(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(data)

    def fill_country(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(data)

    def fill_position(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(data)

    def fill_company(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(data)

    def fill_zip(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(data)

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()
        
    def color_zip(self):
    #получить цвет поля с зип-кодом
        as_is_zip = self._driver.find_element(By.CSS_SELECTOR, "div#zip-code").value_of_css_property("background-color")
        return as_is_zip
    
    def color_firstname(self):
    #получить цвет поля с именем
        as_is_color_firstname = self._driver.find_element(By.CSS_SELECTOR, "div#first-name").value_of_css_property("background-color")
        return as_is_color_firstname
    
    def color_lastname(self):
    #получить цвет поля с фамилией
        as_is_color_lastname = self._driver.find_element(By.CSS_SELECTOR, "div#last-name").value_of_css_property("background-color")
        return as_is_color_lastname
    
    def color_address(self):
    #получить цвет поля с адресом
        as_is_color_address = self._driver.find_element(By.CSS_SELECTOR, "div#address").value_of_css_property("background-color")
        return as_is_color_address
    
    def color_email(self):
    #получить цвет поля с email
        as_is_color_email = self._driver.find_element(By.CSS_SELECTOR, "div#e-mail").value_of_css_property("background-color")
        return as_is_color_email
    
    def color_phone(self):
    #получить цвет поля с телефоном
        as_is_color_phone = self._driver.find_element(By.CSS_SELECTOR, "div#phone").value_of_css_property("background-color")
        return as_is_color_phone
    
    def color_city(self):
    #получить цвет поля с городом
        as_is_color_city = self._driver.find_element(By.CSS_SELECTOR, "div#city").value_of_css_property("background-color")
        return as_is_color_city
    
    def color_country(self):
    #получить цвет поля со страной
        as_is_color_country = self._driver.find_element(By.CSS_SELECTOR, "div#country").value_of_css_property("background-color")
        return as_is_color_country
    
    def color_jobposition(self):
    #получить цвет поля с позицией
        as_is_color_jobposition = self._driver.find_element(By.CSS_SELECTOR, "div#job-position").value_of_css_property("background-color")
        return as_is_color_jobposition
    
    def color_company(self):
    #получить цвет поля с компанией
        as_is_color_company = self._driver.find_element(By.CSS_SELECTOR, "div#company").value_of_css_property("background-color")
        return as_is_color_company  