from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages_1.MainPage import MainPage


def test_color_zip():
    browser = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
    #создаем экз. класса

    main_page = MainPage(browser)
    main_page.fill_form()
    as_is_zip = main_page.color_zip()
    to_be_zip = "rgba(248, 215, 218, 1)"
    assert as_is_zip == to_be_zip
    browser.quit()

def test_other_fields():
    browser = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
    #создаем экз. класса
    main_page = MainPage(browser)
    main_page.fill_form()
    as_is_color_firstname = main_page.color_firstname()
    as_is_color_lastname = main_page.color_lastname()
    as_is_color_address = main_page.color_address()
    as_is_color_email = main_page.color_email()
    as_is_color_phone = main_page.color_phone()
    as_is_color_city = main_page.color_city()
    as_is_color_country = main_page.color_country()
    as_is_color_jobposition = main_page.color_jobposition()
    as_is_color_company = main_page.color_company()
    to_be = "rgba(209, 231, 221, 1)"
    assert as_is_color_firstname == to_be
    assert as_is_color_lastname == to_be
    assert as_is_color_address == to_be
    assert as_is_color_email == to_be
    assert as_is_color_phone == to_be
    assert as_is_color_city == to_be
    assert as_is_color_country == to_be
    assert as_is_color_jobposition == to_be
    assert as_is_color_company == to_be

    browser.quit()