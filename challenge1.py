import unittest
from selenium import webdriver


class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        # self.driver.get("https://www.google.com")
        # self.assertIn("Google", self.driver.title)
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction - Copart USA - Salvage Cars for Sale in Online Car Auctions", self.driver.title)



if __name__ == '__main__':
    unittest.main()