from PageObject.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    product_title = "//h1[@id='product-name-default']"
    product_cart = "//a[@class='link-default clearfix']"
    # btn_buy = "//div[@class='Wrapper-sc-1i9za0i-3 hyuQAM ViewUI-sc-1ijittn-6 iXIDWU']"
    btn_buy = "//a[@id='btn-buy']//span[contains(text(),'Comprar')]"
    btn_confirm = "//span[contains(text(),'Sim, continuar')]"
    btn_size = "//body/div[@id='content']/div[@class='ViewUI-sc-1ijittn-6 iXIDWU']/div[@class='product-page__ViewUI-b5yzc3-0 bhCqWV ViewUI-sc-1ijittn-6 iXIDWU']/div[@class='GridUI-wcbvwm-0 jjjQOQ ViewUI-sc-1ijittn-6 iXIDWU']/div[@class='ColUI-gjy0oc-0 fOIaix ViewUI-sc-1ijittn-6 iXIDWU']/section[@class='product-main-area__CardProduct-sc-9cfglw-0 gYWqKY CardUI-sc-1eg6n71-0 jxqtmm']/div[@class='GridUI-wcbvwm-0 bKWRII ViewUI-sc-1ijittn-6 iXIDWU']/div[@class='GridUI-wcbvwm-0 gpGkIJ ViewUI-sc-1ijittn-6 iXIDWU']/div[@class='ColUI-gjy0oc-0 eukbCO ViewUI-sc-1ijittn-6 iXIDWU']/div[@class='card-variations ViewUI-sc-1ijittn-6 iXIDWU']/div[@class='SpacingUI-pvph4q-0 evWyAC ViewUI-sc-1ijittn-6 iXIDWU']/div[@class='variation-type variations__Variation-sc-1ghvyff-2 iHHuNO SpacingUI-pvph4q-0 hfOTbB ViewUI-sc-1ijittn-6 iXIDWU']/div[@class='variations__Container-sc-1ghvyff-0 kwNwcd ViewUI-sc-1ijittn-6 iXIDWU']/div[2]/div[1]"
    btn_continue = "//span[@class='TextUI-sc-1i9za0i-4 jYYByD TextUI-sc-12tokcy-0 fONnIv']"
    confirm_popup = "//div[@class='Content-sc-1393p9h-7 jlCTMD ViewUI-sc-1ijittn-6 iXIDWU']"
    confirm_text = "//span[contains(text(),'O produto escolhido é')]"
    feature1 = "//div[@id='app']//span[1]//span[1]"
    feature2 = "//span[@class='basket-productDiffs--value'][contains(text(),'G')]"
    radio_warranty = "//body/div[@id='content']/div[@class='ViewUI-sc-1ijittn-6 iXIDWU']/div/main[@class='service-flow']/div[@class='service-flow--divisor']/div[@class='container-fluid']/div[@class='row flow-wrapper service-content']/div[@class='col-sm-9 col-xs-12 services-types']/section[@class='service-type']/div[@class='row']/div[@class='col-xs-12 col-sm-9 service-info']/div[@class='row']/div[@class='col-xs-12 col-sm-9']/div/div[contains(@class,'garantia_estendida-option-1')]/div[@class='togglebox']/header[@class='toggle-header']/label[@class='toggle-label']/span[1]"

    def check_product_cart(self):
        return WebDriverWait(self.driver, 15). \
            until(EC.visibility_of_element_located((By.XPATH, CartPage.product_cart))).text

    def check_product_title(self):
        return WebDriverWait(self.driver, 15). \
            until(EC.visibility_of_element_located((By.XPATH, CartPage.product_title))).text

    def click_buy(self):
        self.driver.find_element_by_xpath(CartPage.btn_buy).click()

    def check_confirm_product(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, CartPage.confirm_popup)))
        return self.driver.find_element_by_xpath(CartPage.confirm_text).text

    def click_confirm_product(self):
        self.driver.find_element_by_xpath(CartPage.btn_confirm).click()

    def check_product_features(self):
        f1 = self.driver.find_element_by_xpath(CartPage.feature1).text
        f2 = self.driver.find_element_by_xpath(CartPage.feature2).text
        return f1 + f2

    def click_product_size(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, CartPage.btn_size))).click()

    def click_radio_warranty(self):
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, CartPage.radio_warranty))).click()

    def click_continue(self):
        self.driver.find_element_by_xpath(CartPage.btn_continue).click()
