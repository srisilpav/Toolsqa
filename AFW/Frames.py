import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class FramesTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/frames")

    def test_frames(self):
        driver = self.driver

        # switch to frames to check the frames are present on the page
        driver.switch_to.frame("frame1")
        element = driver.find_element_by_xpath("//*[@id='sampleHeading']")
        element.is_displayed()
        driver.switch_to.default_content()
        driver.switch_to.frame("frame2")
        element = driver.find_element_by_xpath("//*[@id='sampleHeading']")
        element.is_displayed()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
