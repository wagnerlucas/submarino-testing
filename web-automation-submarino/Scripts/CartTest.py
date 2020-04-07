import unittest
from selenium import webdriver
from Pages.CartPage import CartPage
from Pages.SearchPage import SearchPage
from Data.TestingData import Product


class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Vagno\PycharmProjects\submarino-testing\web"
                                                       r"-automation-submarino\chromedriver.exe")
        self.driver.get("https://www.submarino.com.br/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        SearchPage(self.driver).click_search_bar()

    def tearDown(self):
        self.driver.close()

    def test_add_product_to_cart_successfully(self):
        searchPage = SearchPage(self.driver)
        searchPage.set_search_text(Product.search_valid_product)
        searchPage.press_enter()
        assert Product.title_valid_product, searchPage.check_product_search(Product.title_valid_product)
        searchPage.click_product_search(Product.title_valid_product)

        cartPage = CartPage(self.driver)
        assert Product.title_valid_product, cartPage.check_product_title()

        cartPage.click_buy()
        assert Product.title_valid_product, cartPage.check_product_cart()

    def test_add_product_with_details_to_cart(self):
        searchPage = SearchPage(self.driver)
        searchPage.set_search_text(Product.search_product_with_details)
        searchPage.press_enter()
        assert Product.title_product_with_details, searchPage.check_product_search(Product.title_product_with_details)
        searchPage.click_product_search(Product.title_product_with_details)

        cartPage = CartPage(self.driver)
        assert Product.title_product_with_details, cartPage.check_product_title()
        cartPage.click_buy()
        assert Product.title_product_features, cartPage.check_confirm_product()
        cartPage.click_confirm_product()

        assert Product.title_valid_product, cartPage.check_product_cart()
        assert Product.features_product, cartPage.check_product_features()

    def test_add_product_to_to_cart_with_extended_warranty(self):
        searchPage = SearchPage(self.driver)
        searchPage.set_search_text(Product.search_product_warranty)
        searchPage.press_enter()
        assert Product.title_product_warranty, searchPage.check_product_search(Product.title_product_warranty)
        searchPage.click_product_search(Product.title_product_warranty)

        cartPage = CartPage(self.driver)
        assert Product.title_product_warranty, cartPage.check_product_title()
        cartPage.click_buy()
        cartPage.click_radio_warranty()
        cartPage.click_continue()
        assert Product.title_product_warranty, cartPage.check_product_cart()

    def test_add_product_that_is_no_stock(self):
        searchPage = SearchPage(self.driver)
        searchPage.set_search_text(Product.search_product_no_stock)
        searchPage.press_enter()
        assert Product.title_product_no_stock, searchPage.check_product_search(Product.title_product_no_stock)
        assert Product.message_no_stock, searchPage.check_message_no_stock()
        searchPage.click_product_search(Product.title_product_no_stock)
        assert Product.category_no_stock, searchPage.check_category_no_stock()


if __name__ == '__main__':
    unittest.main()
