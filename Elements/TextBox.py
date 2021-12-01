import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TextBoxTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/text-box")

    def test_textbox(self):
        driver = self.driver
        element = driver.find_element_by_id("userName")
        element.send_keys("Sri Rama")
        element = driver.find_element_by_id("userEmail")
        element.send_keys("srirama@gmail.com")
        element = driver.find_element_by_id("currentAddress")
        element.send_keys("012345 Seshu Seyana complex, vaikunta")
        element = driver.find_element_by_id("permanentAddress")
        element.send_keys("012345 Seshu Seyana complex, vaikunta")
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "submit")))
        driver.find_element_by_id("submit").click()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
