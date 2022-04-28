from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    pass

class LoginPageLocators():
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL_FORM = (By.CSS_SELECTOR, "id_registration-email")
    REGISTRATION_PASSWORD_FORM1 = (By.CSS_SELECTOR, "id_registration-password1")
    REGISTRATION_PASSWORD_FORM2 = (By.CSS_SELECTOR, "id_registration-password2")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOKNAME_ON_CARD = (By.CSS_SELECTOR, "div.product_main > h1")
    BOOKNAME_ON_PUSH = (By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div/strong")
    PRICE_ON_CARD = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRICE_ON_PUSH = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    