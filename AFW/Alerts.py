import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class AlertTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/alerts")

    def test_alerts(self):
        driver = self.driver
        element = driver.find_element_by_id("alertButton")
        element.click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        element = driver.find_element_by_id("timerAlertButton")
        element.click()
        time.sleep(8)
        driver.switch_to.alert.accept()
        element = driver.find_element_by_id("confirmButton")
        element.click()
        driver.switch_to.alert.accept()
        element = driver.find_element_by_id("confirmButton")
        element.click()
        driver.switch_to.alert.dismiss()
        element = driver.find_element_by_id("promtButton")
        element.click()
        driver.switch_to.alert.send_keys("srirama")
        driver.switch_to.alert.accept()
        time.sleep(2)



    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
