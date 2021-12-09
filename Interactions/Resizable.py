import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ResizableTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/resizable")

    def test_resizable(self):
        driver = self.driver
        # resize the boxes both length and width wise
        element = driver.find_element_by_xpath("//*[@id='resizableBoxWithRestriction']/span")
        action = ActionChains(driver)
        action.click_and_hold(element).move_by_offset(65,0).pause(2).move_by_offset(-80,0).pause(2).move_by_offset(82,0).perform()

        element1 = driver.find_element_by_xpath("//*[@id='resizable']/span")
        action = ActionChains(driver)
        action.click_and_hold(element1).move_by_offset(65, 0).pause(2).move_by_offset(-80, 0).pause(2).move_by_offset(82,
                                                                                                                     0).perform()
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
