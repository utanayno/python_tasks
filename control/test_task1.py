from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_fill_form():
    browser = webdriver.Chrome(service=ChromeService((ChromeDriverManager().install())))
    #перейти на сайт
    browser.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    browser.fullscreen_window()
    
    #заполнить форму
    browser.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    browser.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    browser.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    browser.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    browser.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    browser.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    browser.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    browser.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    browser.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")
    browser.implicitly_wait(4)
    #нажать Submit
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

    #проверить, что поле Zip code подсвечено красным
    as_is_zip = browser.find_element(By.CSS_SELECTOR, "div#zip-code").value_of_css_property("background-color")
    to_be_zip = "rgba(248, 215, 218, 1)"
    assert as_is_zip == to_be_zip

    #проверить, что остальные поля подсвечены зеленым
    as_is_color_firstname = browser.find_element(By.CSS_SELECTOR, "div#first-name").value_of_css_property("background-color")
    as_is_color_lastname = browser.find_element(By.CSS_SELECTOR, "div#last-name").value_of_css_property("background-color")
    as_is_color_address = browser.find_element(By.CSS_SELECTOR, "div#address").value_of_css_property("background-color")
    as_is_color_email = browser.find_element(By.CSS_SELECTOR, "div#e-mail").value_of_css_property("background-color")
    as_is_color_phone = browser.find_element(By.CSS_SELECTOR, "div#phone").value_of_css_property("background-color")
    as_is_color_city = browser.find_element(By.CSS_SELECTOR, "div#city").value_of_css_property("background-color")
    as_is_color_country = browser.find_element(By.CSS_SELECTOR, "div#country").value_of_css_property("background-color")
    as_is_color_jobposition = browser.find_element(By.CSS_SELECTOR, "div#job-position").value_of_css_property("background-color")
    as_is_color_company = browser.find_element(By.CSS_SELECTOR, "div#company").value_of_css_property("background-color")

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
    
    