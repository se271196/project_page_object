from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.locators import MainLinkLocators
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import pytest

#["the-shellcoders-handbook_209/?promo=newYear","coders-at-work_207/?promo=newYear2019"]
@pytest.mark.parametrize('name',["coders-at-work_207/?promo=offer0",
                                  "coders-at-work_207/?promo=offer1",
                                  "coders-at-work_207/?promo=offer2",
                                  "coders-at-work_207/?promo=offer3",
                                  "coders-at-work_207/?promo=offer4",
                                  "coders-at-work_207/?promo=offer5",
                                  "coders-at-work_207/?promo=offer6",
                                  "coders-at-work_207/?promo=offer7",
                                  "coders-at-work_207/?promo=offer8",
                                  "coders-at-work_207/?promo=offer9"] )
def  test_guest_can_add_product_to_basket(browser,name):
   link=f"{MainLinkLocators.CATALOGUE_LINK}{name}"
   page = ProductPage(browser, link)
   page.open()
   page.click_buy()
   page.solve_quiz_and_get_code()
#для ниндзя
   text = browser.find_element(By.CSS_SELECTOR, "#messages>div:nth-child(1)>div ").text
   print(text)
   assert text=='Coders at Work был добавлен в вашу корзину.', 'несовпадают'



