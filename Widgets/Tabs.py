import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TabTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/tabs")

    def test_tabs(self):
        driver = self.driver

        # check the tabs by clicking on them
        element = driver.find_element_by_id("demo-tab-origin")
        element.click()
        element = driver.find_element_by_id("demo-tab-use")
        element.click()
        element = driver.find_element_by_id("demo-tab-what")
        element.click()
        element = driver.find_element_by_id("demo-tab-use")
        element.click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
