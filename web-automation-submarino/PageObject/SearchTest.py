import unittest
from selenium import webdriver
from PageObject.SearchPage import SearchPage
from PageObject.Data import Product
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SearchTestCase(unittest.TestCase):

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

    def test_search_product_successfully(self):
        searchPage = SearchPage(self.driver)
        searchPage.set_search_text(Product.search_valid_product)
        searchPage.press_enter()
        assert Product.title_valid_product in searchPage.check_product_search(Product.title_valid_product)

    def test_search_product_with_incomplete_name(self):
        searchPage = SearchPage(self.driver)
        searchPage.set_search_text(Product.search_product_incomplete)
        searchPage.press_enter()
        assert Product.message_alternative_results, searchPage.check_message_alternative_results()
        assert Product.title_alternative_product, searchPage.check_product_search(Product.title_alternative_product)

    def test_search_product_with_wrong_name(self):
        searchPage = SearchPage(self.driver)
        searchPage.set_search_text(Product.search_product_wrong)
        searchPage.press_enter()
        assert Product.message_alternative_results, searchPage.check_message_alternative_results()
        assert Product.title_alternative_product, searchPage.check_product_search(Product.title_alternative_product)

    def test_search_product_with_no_results_found(self):
        searchPage = SearchPage(self.driver)
        searchPage.set_search_text(Product.search_product_not_found)
        searchPage.press_enter()
        assert Product.message_not_found, searchPage.check_message_not_found()

    def test_search_suggested_product(self):
        searchPage = SearchPage(self.driver)
        searchPage.set_search_text(Product.search_product_suggested)
        assert Product.title_product_suggested1, searchPage.check_product_search(Product.title_product_suggested1)
        assert Product.title_product_suggested2, searchPage.check_product_search(Product.title_product_suggested2)
        assert Product.title_product_suggested3, searchPage.check_product_search(Product.title_product_suggested3)

    def test_search_for_a_product_that_is_no_stock(self):
        searchPage = SearchPage(self.driver)
        searchPage.set_search_text(Product.search_product_no_stock)
        searchPage.press_enter()
        assert Product.title_product_no_stock, searchPage.check_product_search(Product.title_product_no_stock)
        assert Product.message_no_stock, searchPage.check_message_no_stock()


if __name__ == '__main__':
    unittest.main()
