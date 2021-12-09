import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ProgressBarTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/progress-bar")

    def test_progressBar(self):
        driver = self.driver

        # check the progress bar functionality
        element = driver.find_element_by_id("startStopButton")
        element.click()
        time.sleep(2)
        element.click()
        time.sleep(2)
        element.click()
        time.sleep(2)
        element.click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
