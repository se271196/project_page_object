from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.locators import MainLinkLocators
from .pages.login_page import LoginPage

def  test_guest_can_add_product_to_basket(browser):
   link=" http: // selenium1py.pythonanywhere.com / ru / catalogue / the - shellcoders - handbook_209 /?promo = newYear"
   page = ProductPage(browser, link)
   page.open()

