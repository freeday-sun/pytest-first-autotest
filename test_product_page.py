import pytest
from .pages.product_page import ProductPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        ]


@pytest.mark.parametrize("product", links)
def test_guest_can_add_product_to_basket(browser, product):
    link = product
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_must_be_added_to_basket()
    page.product_price_equal_basket_amount()


