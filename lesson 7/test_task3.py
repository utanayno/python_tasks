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
    main_page.authorization_user("standard_user")
    main_page.authorization_password("secret_sauce")
    main_page.authorization_submit()
    
    main_page.add_to_cart()
    cart_page = CartPage(browser)
    cart_page.click_checkout()
    
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_checkout_name("Julia")
    checkout_page.fill_checkout_lastname("Tanayno")
    checkout_page.fill_checkout_postalcode("3029")
    checkout_page.checkout_continue()
    
    
    result = checkout_page.get_total()
    expected_result = "Total: $58.29"
    assert result == expected_result
    browser.quit() 