import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class DatePickerTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/date-picker")

    def test_datePicker(self):
        driver = self.driver

        # select the date and time
        element = driver.find_element_by_xpath("//*[@id='datePickerMonthYearInput']")
        element.send_keys(10 * Keys.BACK_SPACE)
        element.send_keys('02/01/2021')
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        element = driver.find_element_by_xpath("//*[@id='dateAndTimePickerInput']")
        element.send_keys(25 * Keys.BACK_SPACE)
        element.send_keys('December 28, 2016 02:53 AM')
        element.send_keys(Keys.RETURN)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
