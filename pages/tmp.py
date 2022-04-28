import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
browser = webdriver.Chrome()
browser.get(link)
add_to_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
add_to_basket.click()

#alert = browser.switch_to.alert
#x = alert.text.split(" ")[2]
#answer = str(math.log(abs((12 * math.sin(float(x))))))
#alert.send_keys(answer)
#alert.accept()
#try:
#    alert = browser.switch_to.alert
#    alert_text = alert.text
#    print(f"Your code: {alert_text}")
#    alert.accept()
#except NoAlertPresentException:
#    print("No second alert presented")

assert browser.is_not_element_present(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div/strong"), "Элемент отсутствует!"

#card_book_name = browser.find_element(By.CSS_SELECTOR, "div.product_main > h1")
#push_book_name = browser.find_element(By.XPATH, "//*[@id='messages']/div[1]/div/strong")
#assert card_book_name.text == push_book_name.text, "Название книги другое"
#
#card_book_price = browser.find_element(By.CSS_SELECTOR, "div.product_main p.price_color")
#push_book_price = browser.find_element(By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
#assert card_book_name.text == push_book_name.text, "Цена другая"