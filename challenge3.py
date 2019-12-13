import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")


    def tearDown(self):
        self.driver.close()

    def test_challege3forLoop(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        for a in self.driver.find_elements(By.XPATH, "//*[@ng-if='popularSearches']//a"):
            print(a.text + " - " + a.get_attribute('href'))


if __name__ == '__main__':
    unittest.main()