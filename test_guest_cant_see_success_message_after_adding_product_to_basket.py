import pytest
from .pages.product_page import ProductPage

@pytest.mark.xfail(reason="fixing this bug right now")
def test_add_basket_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_element_present()