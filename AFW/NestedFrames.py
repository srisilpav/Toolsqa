import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class NestedFrameTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/nestedframes")

    def test_nestedFrames(self):
        driver = self.driver
        driver.switch_to.frame("frame1")
        element = driver.find_element_by_tag_name("body")
        print(element.text)
        driver.switch_to.default_content()
        element= driver.find_element_by_xpath("/html/body/iframe")
        driver.switch_to.frame(element)
        element = driver.find_element_by_xpath("/html")
        print(element.is_displayed())
        textInside = element.text
        print(textInside)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
