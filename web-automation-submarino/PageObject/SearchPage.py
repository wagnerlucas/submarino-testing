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
    product_no_stock = "//h2[contains(text(),'Game - FIFA 20 Edição dos Campeões - XBOX ONE')]"

    message_alternative_results = "//h1[@class='h3']"
    message_not_found = "//span[@class='TextUI-sc-12tokcy-0 CIZtP']"
    message_no_stock = "//div[@class='row product-grid no-gutters main-grid']//div[1]//div[1]//div[2]//a[1]//section[" \
                       "1]//div[2]//div[2]//span[1] "

    def click_search_bar(self):
        self.driver.find_element_by_xpath(SearchPage.search_bar).click()

    def set_search_text(self, search_text):
        search = self.driver.find_element_by_xpath(SearchPage.search_bar)
        search.send_keys(search_text)

    def press_enter(self):
        search = self.driver.find_element_by_xpath(SearchPage.search_bar)
        search.send_keys(Keys.ENTER)

    def check_product_search(self, product):
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
        else:
            path = ""

        product_title = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, path)))

        return product_title.text

    def check_message_alternative_results(self):
        return self.driver.find_element_by_xpath(SearchPage.message_alternative_results).text

    def check_message_not_found(self):
        return self.driver.find_element_by_xpath(SearchPage.message_not_found).text

    def check_message_no_stock(self):
        return self.driver.find_element_by_xpath(SearchPage.message_no_stock).text
