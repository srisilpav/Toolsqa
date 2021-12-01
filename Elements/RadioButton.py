import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class RadioButtonTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/radio-button")

    def test_radiobutton(self):
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[1]/div[2]/label")
        element.click()
        element = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[1]/div[3]/label")
        element.click()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
