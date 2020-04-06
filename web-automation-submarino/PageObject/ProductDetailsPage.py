from PageObject.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObject.Data import Product


class ProductDetailsPage(BasePage):
    product_title = "//h1[@id='product-name-default']"
    btn_buy = "//div[@class='Wrapper-sc-1i9za0i-3 hyuQAM ViewUI-sc-1ijittn-6 iXIDWU']"
