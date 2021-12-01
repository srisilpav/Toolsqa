import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class DynamicPropertiesTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/dynamic-properties")

    def test_dynamicProperties(self):
        driver = self.driver
        element = driver.find_element_by_id("enableAfter")
        print(element.is_enabled())
        element = driver.find_element_by_id("colorChange")
        print(element.get_attribute("class"))

        if element.get_attribute("class") == "mt-4 btn btn-primary":
            print("color change is in red color")
        else:
            print("color changed to red")
        element = driver.find_element_by_id("enableAfter")
        print(element.is_displayed())
        time.sleep(5)
        element = driver.find_element_by_id("enableAfter")
        print(element.is_enabled())
        element = driver.find_element_by_id("colorChange")
        print(element.get_attribute("class"))

        if element.get_attribute("class") == "mt-4 text-danger btn btn-primary":
            print("color change is in white color")
        else:
            print("color changed to red")
        element = driver.find_element_by_id("enableAfter")
        print(element.is_displayed())

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
