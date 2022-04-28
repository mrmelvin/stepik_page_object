from selenium.common.exceptions import NoAlertPresentException
import math
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_to_basket.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")  

    def check_bookname(self):
        card_book_name = self.browser.find_element(*ProductPageLocators.BOOKNAME_ON_CARD)
        push_book_name = self.browser.find_element(*ProductPageLocators.BOOKNAME_ON_PUSH)
        assert card_book_name.text == push_book_name.text, "Добавлена не та книга!"
        #card_book_price = self.browser.find_element(*ProductPageLocators.PRICE_ON_CARD)
        #push_book_price = self.browser.find_element(*ProductPageLocators.PRICE_ON_PUSH)        
        #assert card_book_price.text == push_book_price.text, "Цена отличается!"


    def should_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOKNAME_ON_PUSH), "Элемент отсутствует!" 

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BOOKNAME_ON_PUSH), "Элемент не исчезает!"