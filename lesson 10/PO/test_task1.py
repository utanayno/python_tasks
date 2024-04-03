from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
import allure

from pages_1.MainPage import MainPage

@allure.title("Проверка цвета поля почтового индекса (поле не заполнено)")
@allure.description("Проверить, что если поле не заполнить, то оно подсветится красным цветом")
@allure.feature("READ")
@allure.severity("normal")
def test_color_zip():
    browser = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
    
    main_page = MainPage(browser)
    main_page.fill_first_name("Иван")
    main_page.fill_last_name("Петров")
    main_page.fill_address("Ленина, 55-3")
    main_page.fill_email("test@skypro.com")
    main_page.fill_phone("+7985899998787")
    main_page.fill_zip("")
    main_page.fill_city("Москва")
    main_page.fill_country("Россия")
    main_page.fill_position("QA")
    main_page.fill_company("SkyPro")
    main_page.submit()
      
    as_is_color_zip = main_page.color_zip()
    to_be_color_zip = "rgba(248, 215, 218, 1)"
    with allure.step("Проверить, что цвет поля с почтовым кодом - красный"):
        assert as_is_color_zip == to_be_color_zip
    browser.quit()

@allure.title("Проверка цвета полей формы (поля заполнены валидными данными)")
@allure.description("Проверить, что если поля формы заполнить валидными данными, то они подсветятся зеленым цветом")
@allure.feature("READ")
@allure.severity("critical")
def test_other_fields():
    browser = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
    
    main_page = MainPage(browser)
    main_page.fill_first_name("Иван")
    main_page.fill_last_name("Петров")
    main_page.fill_address("Ленина, 55-3")
    main_page.fill_email("test@skypro.com")
    main_page.fill_phone("+7985899998787")
    main_page.fill_city("Москва")
    main_page.fill_country("Россия")
    main_page.fill_position("QA")
    main_page.fill_company("SkyPro")
    main_page.submit()
    to_be_color = "rgba(209, 231, 221, 1)"
    with allure.step("Проверить, что цвет поля с именем - зеленый"):
        assert main_page.color_firstname() == to_be_color
    with allure.step("Проверить, что цвет поля с фамилией - зеленый"):
        assert main_page.color_lastname() == to_be_color
    with allure.step("Проверить, что цвет поля с адресом - зеленый"):
        assert main_page.color_address() == to_be_color
    with allure.step("Проверить, что цвет поля с эл. почтой - зеленый"):
        assert main_page.color_email() == to_be_color
    with allure.step("Проверить, что цвет поля с телефоном - зеленый"):
        assert main_page.color_phone() == to_be_color
    with allure.step("Проверить, что цвет поля с городом - зеленый"):
        assert main_page.color_city() == to_be_color
    with allure.step("Проверить, что цвет поля со страной - зеленый"):
        assert main_page.color_country() == to_be_color
    with allure.step("Проверить, что цвет поля с позицией - зеленый"):
        assert main_page.color_jobposition() == to_be_color
    with allure.step("Проверить, что цвет поля с компанией - зеленый"):
        assert main_page.color_company() == to_be_color

    browser.quit()