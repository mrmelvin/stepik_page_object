import pytest
from .pages.product_page import ProductPage
from time import sleep


#@pytest.mark.parametrize("link", [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10)])
#def test_guest_can_add_product_to_basket(browser, link):
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_basket()
#    page.solve_quiz_and_get_code()
#    page.check_bookname()
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
        