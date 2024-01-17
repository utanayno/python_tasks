from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from pages_3.MainPage import MainPage
from pages_3.CartPage import CartPage
from pages_3.CheckoutPage import CheckoutPage

def test_total():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.authorization()
    browser.implicitly_wait(5)
    main_page.add_to_cart()
    cart_page = CartPage(browser)
    cart_page.click_checkout()
    browser.implicitly_wait(5)
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_checkout()
    result = checkout_page.get_total()
    assert result == "Total: $58.29"
    browser.quit() 