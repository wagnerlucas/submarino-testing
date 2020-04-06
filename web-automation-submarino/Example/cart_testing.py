import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Vagno\PycharmProjects\submarino-testing\web"
                                                       r"-automation-submarino\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.close()

    def test_add_product_to_cart_successfully(self):
        product_title_compare = "Game Fifa 20 Standard Edition - PS4"

        driver = self.driver
        driver.get("https://www.submarino.com.br/")

        search = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='h_search-input']")))
        search.click()
        search.send_keys("fifa 20")
        search.send_keys(Keys.ENTER)

        product_search = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Game Fifa 20 Standard Edition - PS4')]")))
        assert product_title_compare in product_search.text
        product_search.click()

        product_title_details = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//h1[@id='product-name-default']")))
        assert product_title_compare in product_title_details.text

        btn_buy_details = driver.find_element_by_xpath("//div[@class='Wrapper-sc-1i9za0i-3 hyuQAM ViewUI-sc-1ijittn-6 iXIDWU']")
        btn_buy_details.click()

        product_title_cart = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((
            By.XPATH, "//a[@class='link-default clearfix']")))
        assert product_title_compare in product_title_cart.text


if __name__ == '__main__':
    unittest.main()
