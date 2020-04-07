from PageObject.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObject.Data import Product


class SearchPage(BasePage):
    search_bar = "//input[@id='h_search-input']"

    product_valid = "//h2[contains(text(),'Game Fifa 20 Standard Edition - PS4')]"
    product_alternative = "//h2[contains(text(),'Console Playstation 4 Pro 1 TB + Controle Wireless')]"
    product_suggested1 = "//span[contains(text(),'Console Ps4 1TB + 3 Jogos + Voucher Fortnite + Con')]"
    product_suggested2 = "//span[contains(text(),'Console PS4 1TB Edição Family')]"
    product_suggested3 = "//span[contains(text(),'+ Controle Wireless Dua')]"
    product_no_stock = "//h2[contains(text(),'Álcool Gel Antisséptico 70º | 60 gramas | Caixa co')]"
    product_with_details = "//h2[contains(text(),'Camisa Hering Manga Longa Jeans Feminina')]"
    product_warranty = "//h2[contains(text(),'Bicicleta Ergométrica Polimet BP-880 - Preta com 6')]"

    message_alternative_results = "//h1[@class='h3']"
    message_not_found = "//span[@class='TextUI-sc-12tokcy-0 CIZtP']"
    message_no_stock = "//span[@class='UnavailableTextMessage-bwhjk3-17 bpHuDW TextUI-sc-12tokcy-0 CIZtP']"

    category_no_stock = "//h1[@class='category-title']"

    def click_search_bar(self):
        self.driver.find_element_by_xpath(SearchPage.search_bar).click()

    def set_search_text(self, search_text):
        search = self.driver.find_element_by_xpath(SearchPage.search_bar)
        search.send_keys(search_text)

    def press_enter(self):
        search = self.driver.find_element_by_xpath(SearchPage.search_bar)
        search.send_keys(Keys.ENTER)

    def check_product_search(self, product):
        path = self.get_product_path(product)
        product_title = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, path)))

        return product_title.text

    def check_message_alternative_results(self):
        return self.driver.find_element_by_xpath(SearchPage.message_alternative_results).text

    def check_message_not_found(self):
        return self.driver.find_element_by_xpath(SearchPage.message_not_found).text

    def check_message_no_stock(self):
        return self.driver.find_element_by_xpath(SearchPage.message_no_stock).text

    def click_product_search(self, product):
        path = self.get_product_path(product)
        prod = WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, path)))
        prod.click()

    def check_category_no_stock(self):
        return WebDriverWait(self.driver, 25).\
            until(EC.element_to_be_clickable((By.XPATH, SearchPage.category_no_stock))).text

    @staticmethod
    def get_product_path(product):
        if product == Product.title_valid_product:
            path = SearchPage.product_valid
        elif product == Product.title_alternative_product:
            path = SearchPage.product_alternative
        elif product == Product.title_product_suggested1:
            path = SearchPage.product_suggested1
        elif product == Product.title_product_suggested2:
            path = SearchPage.product_suggested2
        elif product == Product.title_product_suggested3:
            path = SearchPage.product_suggested3
        elif product == Product.title_product_no_stock:
            path = SearchPage.product_no_stock
        elif product == Product.title_product_with_details:
            path = SearchPage.product_with_details
        elif product == Product.title_product_warranty:
            path = SearchPage.product_warranty
        else:
            path = SearchPage.product_no_stock
        return path
