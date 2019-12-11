import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec



class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction - Copart USA - Salvage Cars for Sale in Online Car Auctions", self.driver.title)
        self.driver.find_element(By.XPATH, "//input['input-search']").send_keys("exotics")
        searchBtn = ec.element_to_be_clickable((By.XPATH,  "//button[@class='btn btn-lightblue marginleft15']"))
        wait(self.driver, 20).until(searchBtn)
        self.driver.find_element_by_xpath("//button[@class='btn btn-lightblue marginleft15']").click()
        element = ec.presence_of_all_elements_located((By.XPATH,"//input[@class='form-control input-sm']"))
        wait(self.driver, 40).until(element)
        car = self.driver.find_element_by_xpath(("//table[@id='serverSideDataTable']")).text
        self.assertIn("PORSCHE",car)

if __name__ == '__main__':
    unittest.main()





