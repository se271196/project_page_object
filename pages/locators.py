from selenium.webdriver.common.by import By

#only for elements page
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

#only for url
class MainLinkLocators():
    MAIN_LINK="http://selenium1py.pythonanywhere.com/"
    LOGIN_LING=f"{MAIN_LINK}/accounts/login/"
    #http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear
