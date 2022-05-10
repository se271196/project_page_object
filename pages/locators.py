from selenium.webdriver.common.by import By

#only for elements page
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    BUTTON_ADD_TO_BASKET=By.CSS_SELECTOR,'button.btn-add-to-basket'


#only for url
class MainLinkLocators():
    MAIN_LINK="http://selenium1py.pythonanywhere.com/"
    LOGIN_LING=f"{MAIN_LINK}/accounts/login/"
    CATALOGUE_LINK=f"{MAIN_LINK}/catalogue/"
    #http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear
