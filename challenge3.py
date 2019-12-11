import unittest
from selenium import webdriver
from bs4 import BeautifulSoup


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challege3(self):
        self.driver.get("https://www.copart.com")

    def test_challenge3forLoop(self):
        Cars = ["ALTIMA", "SILVERADO", "TOYOTA HYUNDAI", "SONATA", "SENTRA", "FORD", "VOLVO", "COROLLA", "CHARGER",
                "HONDA",
                "BMW", "CAMRY", "ODYSSEY EX", "NISSAN",
                "DODGE", "ACCORD EX", "F150 SUPER", "CHEVROLET", "KIA"]
        for temp in Cars:
            self.driver.find_element_by_xpath("//table[@id='serverSideDataTable']")
            print temp


     # self.driver.find_element_by_xpath("//div[@id='tabTrending']")





    #  // *[ @ id = "tabTrending"] / div[1] / div[2] / div[2] / ul / li[3] / a

    # def test_challenge3whileLoop(self):
    # Cars = ["ALTIMA", "SILVERADO", "TOYOTA HYUNDAI", "SONATA", "SENTRA", "FORD", "VOLVO", "COROLLA", "CHARGER",
    #        "HONDA", "BMW", "CAMRY", "ODYSSEY EX", "NISSAN",
    #        "DODGE", "ACCORD EX", " F150 SUPER", "CHEVROLET", "KIA"]
    # print Cars

    # self.driver.get("https://www.copart.com")


if __name__ == '__main__':
    unittest.main()
