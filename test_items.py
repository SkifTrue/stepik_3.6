from selenium.webdriver.common.by import By


def test_add_to_cart_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(10)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button is not None, "Button to add item to basket is not found"
