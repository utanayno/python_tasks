from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager

from pages_1.MainPage import MainPage


def test_color_zip():
    browser = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
    #создаем экз. класса

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
    assert as_is_color_zip == to_be_color_zip
    browser.quit()

def test_other_fields():
    browser = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
    #создаем экз. класса
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
    to_be_color = "rgba(209, 231, 221, 1)"
    assert main_page.color_firstname() == to_be_color
    assert main_page.color_lastname() == to_be_color
    assert main_page.color_address() == to_be_color
    assert main_page.color_email() == to_be_color
    assert main_page.color_phone() == to_be_color
    assert main_page.color_city() == to_be_color
    assert main_page.color_country() == to_be_color
    assert main_page.color_jobposition() == to_be_color
    assert main_page.color_company() == to_be_color

    browser.quit()