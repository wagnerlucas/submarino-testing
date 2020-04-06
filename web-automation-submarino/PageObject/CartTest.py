import unittest
from selenium import webdriver
from PageObject.ProductDetailsPage import SearchPage
from PageObject.Data import Product
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Vagno\PycharmProjects\submarino-testing\web"
                                                       r"-automation-submarino\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
