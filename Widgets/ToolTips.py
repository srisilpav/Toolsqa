import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ToolTipTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/tool-tips")

    def test_tooltip(self):
        driver = self.driver

        # Hoover over the button anf input box
        element = driver.find_element_by_id("toolTipButton")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        time.sleep(2)
        element = driver.find_element_by_id("texFieldToolTopContainer")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
