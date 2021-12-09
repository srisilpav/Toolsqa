import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ModalTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/modal-dialogs")

    def test_modals(self):
        driver = self.driver

        # click on the "Small modal" button to open the small modal and then close the modal.
        element = driver.find_element_by_xpath("//*[@id='showSmallModal']")
        element.click()
        element = driver.find_element_by_id("closeSmallModal")
        element.click()

        # click on the "Large modal" button to open the large modal and then close the modal.
        element = driver.find_element_by_id("showLargeModal")
        element.click()
        element = driver.find_element_by_id("closeLargeModal")
        element.click()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
