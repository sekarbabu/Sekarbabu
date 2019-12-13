import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

    def tearDown(self):
        self.driver.close()

    # def test_challege3forLoop(self):
    #     elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]/a")
    #     print(len(elements))
    #     for count in elements:
    #         print (count.text + ": " + count.get_attribute("href"))

    def test_challege3whileLoop(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]/a")
        print(len(elements))
        i = 0
        while i < len(elements):
            print (elements[i].text + ": " + elements[i].get_attribute("href"))
            i += 1


        # Print Makes/Models list and Url's

        #for a in self.driver.find_elements(By.XPATH, "//*[@ng-if='popularSearches']//a"):
        #    print(a.text + " - " + a.get_attribute('href'))



if __name__ == '__main__':
    unittest.main()