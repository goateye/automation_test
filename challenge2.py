import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time



class challenge1(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("./chromedriver")


    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge2(self):
    #code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        self.driver.find_element_by_id("input-search").click()
        self.driver.find_element_by_id("input-search").send_keys("exotics")

        self.driver.find_element_by_id("input-search").send_keys(Keys.ENTER)
        time.sleep(10)

        pagedata = self.driver.find_element_by_id("serverSideDataTable")

        self.assertIn("PORSCHE", pagedata.text)
        #elem.clear()
        #elem.send_keys("test")
        #elem.send_keys(Keys.RETURN)

if __name__ == '__main__':
    unittest.main()
