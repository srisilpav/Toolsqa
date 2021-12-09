import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BrowserWindowTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/browser-windows")

    def test_browserWindow(self):
        driver = self.driver

        # click on the "New Tab" button to open a new tab
        element = driver.find_element_by_id("tabButton")
        element.click()

        # change the window handle to newly opened page and close that page . Then come back to current window
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        element = driver.find_element_by_id("sampleHeading")
        print(element.is_displayed())
        driver.close()
        driver.switch_to.window(window_before)

        # click on the "New Window" button to open the new window.
        # Change the window handle to newly opened window and close that window. Then come back to current window
        element = driver.find_element_by_id("windowButton")
        element.click()
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        element = driver.find_element_by_id("sampleHeading")
        print(element.is_displayed())
        driver.close()
        driver.switch_to.window(window_before)

        # click on the "New Window Message" button to open a window new message.
        # Change  the window handle to newly opened window and close that window. Then come back to current window
        element = driver.find_element_by_id("messageWindowButton")
        element.click()
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.close()
        driver.switch_to.window(window_before)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
