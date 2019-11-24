import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", \
                                         pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(promo_offer)
    print(link)
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_must_be_added_to_basket()
    page.product_price_equal_basket_amount()


