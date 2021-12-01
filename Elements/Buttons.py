import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ButtonTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/buttons")

    def test_textbox(self):
        driver = self.driver
        element = driver.find_element_by_id("doubleClickBtn")
        action = ActionChains(driver)
        action.double_click(element).perform()
        element = driver.find_element_by_id("rightClickBtn")
        action = ActionChains(driver)
        action.context_click(element).perform()
        element = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[1]/div[3]")
        element.click()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
