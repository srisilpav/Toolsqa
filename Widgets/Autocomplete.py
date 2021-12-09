import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class AutoCompleteTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/auto-complete")

    def test_autoComplete(self):
        driver = self.driver

        # check the auto-complete functionality
        element = driver.find_element_by_xpath("//*[@id='autoCompleteMultipleInput']")
        element.send_keys("Yellow")
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.RETURN)
        element.send_keys("green")
        element.send_keys(Keys.RETURN)
        element.send_keys("blue")
        element.send_keys(Keys.RETURN)
        element.send_keys("orange")
        element.send_keys(Keys.RETURN)
        element = driver.find_element_by_xpath("//*[@id='autoCompleteSingleInput']")
        element.send_keys("Green")
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.RETURN)
        element.send_keys("orange")
        element.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
