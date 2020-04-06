import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SearchTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Vagno\PycharmProjects\submarino-testing\web"
                                                       r"-automation-submarino\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.close()

    def test_search_product_successfully(self):
        driver = self.driver
        driver.get("https://www.submarino.com.br/")
        self.driver.implicitly_wait(20)

        search = driver.find_element_by_xpath("//input[@id='h_search-input']")
        search.send_keys("fifa 20")
        search.send_keys(Keys.ENTER)

        driver.get("https://www.submarino.com.br/busca/fifa-20")
        self.driver.implicitly_wait(20)

        self.assertIn("Game Fifa 20 Standard Edition - PS4",
                      driver.find_element_by_xpath("//div[@class='product-grid-item ColUI-gjy0oc-0 ifczFg "
                                                   "ViewUI-sc-1ijittn-6 iXIDWU']//h2[@class='TitleUI-bwhjk3-15 khKJTM "
                                                   "TitleH2-sc-1wh9e1x-1 fINzxm'][contains(text(),'Game Fifa 20 "
                                                   "Standard Edition - PS4')]").text)

    def test_search_product_with_incomplete_name(self):
        driver = self.driver
        driver.get("https://www.submarino.com.br/")
        self.driver.implicitly_wait(20)

        search = driver.find_element_by_xpath("//input[@id='h_search-input']")
        search.send_keys("playstati")
        search.send_keys(Keys.ENTER)

        driver.get("https://www.submarino.com.br/busca/playstati")
        self.driver.implicitly_wait(20)

        self.assertIn("Exibindo resultados para: playstation",
                      driver.find_element_by_xpath("//h1[@class='h3']").text)

        self.assertIn("Console Playstation 4 1TB + Controle Wireless DualShock 4 Edição Limitada Days Of Play",
                      driver.find_element_by_xpath("//div[@class='row product-grid no-gutters main-grid']//div["
                                                   "1]//div[1]//div[2]//a[1]//section[1]//div[2]//div[1]//h2[1]").text)

    def test_search_product_with_wrong_name(self):
        driver = self.driver
        driver.get("https://www.submarino.com.br/")
        self.driver.implicitly_wait(20)

        search = driver.find_element_by_xpath("//input[@id='h_search-input']")
        search.send_keys("praystation")
        search.send_keys(Keys.ENTER)

        driver.get("https://www.submarino.com.br/busca/praystation")
        self.driver.implicitly_wait(20)

        self.assertIn("Exibindo resultados para: playstation",
                      driver.find_element_by_xpath("//h1[@class='h3']").text)

        self.assertIn("Console Playstation 4 1TB + Controle Wireless DualShock 4 Edição Limitada Days Of Play",
                      driver.find_element_by_xpath("//div[@class='row product-grid no-gutters main-grid']//div["
                                                   "1]//div[1]//div[2]//a[1]//section[1]//div[2]//div[1]//h2[1]").text)

    def test_search_product_with_no_results_found(self):
        driver = self.driver
        driver.get("https://www.submarino.com.br/")
        self.driver.implicitly_wait(20)

        search = driver.find_element_by_xpath("//input[@id='h_search-input']")
        search.send_keys("otorinolaringologista")
        search.send_keys(Keys.ENTER)

        driver.get("https://www.submarino.com.br/busca/otorinolaringologista")
        self.driver.implicitly_wait(20)

        self.assertIn("Não encontramos nenhum resultado para \"otorinolaringologista\" em nossos mundos.",
                      driver.find_element_by_xpath("//span[@class='TextUI-sc-12tokcy-0 CIZtP']").text)

    def test_search_suggested_product(self):
        driver = self.driver
        driver.get("https://www.submarino.com.br/")
        self.driver.implicitly_wait(20)

        search = driver.find_element_by_xpath("//input[@id='h_search-input']")
        search.send_keys("playsta")

        self.assertIn("Console Ps4 1TB + 3 Jogos + Voucher Fortnite + Controle DualShock 4 Bundle Hits 6 - Sony",
                      driver.find_element_by_xpath("//span[contains(text(),'Console Ps4 1TB + 3 Jogos + Voucher "
                                                   "Fortnite + Con')]").text)

        self.assertIn("Console PS4 1TB Edição Family",
                      driver.find_element_by_xpath("//span[contains(text(),'Console PS4 1TB Edição Family')]").text)

        self.assertIn("Console Playstation 4 1TB + Controle Wireless DualShock 4 Edição Limitada Days Of Play",
                      driver.find_element_by_xpath("//span[contains(text(),'+ Controle Wireless Dua')]").text)

    def test_search_for_a_product_that_is_no_stock(self):
        driver = self.driver
        driver.get("https://www.submarino.com.br/")
        self.driver.implicitly_wait(20)

        search = driver.find_element_by_xpath("//input[@id='h_search-input']")
        search.send_keys("fifa 20 edição dos campeões XBOX ONE")
        search.send_keys(Keys.ENTER)

        driver.get("https://www.submarino.com.br/busca/fifa-20-edicao-dos-campeoes-xbox-one?rc=fifa+20+edi%C3%A7%C3"
                   "%A3o+dos+campe%C3%B5es+XBOX+ONE")

        self.driver.implicitly_wait(20)

        self.assertIn("Game - FIFA 20 Edição dos Campeões - XBOX ONE",
                      driver.find_element_by_xpath("//h2[contains(text(),'Game - FIFA 20 Edição dos Campeões - XBOX "
                                                   "ONE')]").text)

        self.assertIn("Ops! Já vendemos todo o estoque.",
                      driver.find_element_by_xpath("//div[@class='row product-grid no-gutters main-grid']//div["
                                                   "1]//div[1]//div[2]//a[1]//section[1]//div[2]//div[2]//span["
                                                   "1]").text)


if __name__ == '__main__':
    unittest.main()

