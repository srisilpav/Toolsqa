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

        # Fill all details of the form and submit by clicking "submit" button
        element = driver.find_element_by_id("userName")
        element.send_keys("Sri Rama")
        element = driver.find_element_by_id("userEmail")
        element.send_keys("srirama@gmail.com")
        element = driver.find_element_by_id("currentAddress")
        element.send_keys("012345 Seshu Seyana complex, vaikunta")
        element = driver.find_element_by_id("permanentAddress")
        element.send_keys("012345 Seshu Seyana complex, vaikunta")
        
        # WebDriverWait(driver,3000).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
        # time.sleep method suspends execution for the given number of seconds. It is not recommended to use it though.
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
