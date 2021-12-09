import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WebTableTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/webtables")

    def test_webTable(self):
        driver = self.driver

        # Add an entry too the table by clicking on "Add" button.
        element = driver.find_element_by_id("addNewRecordButton")
        element.click()
        element = driver.find_element_by_id("firstName")
        element.send_keys("Sri Rama")
        element = driver.find_element_by_id("lastName")
        element.send_keys("Antharathma")
        element = driver.find_element_by_id("userEmail")
        element.send_keys("srirama@gmail.com")
        element = driver.find_element_by_id("age")
        element.send_keys("100")
        element = driver.find_element_by_id("salary")
        element.send_keys("1000000")
        element = driver.find_element_by_id("department")
        element.send_keys("god")
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "submit")))
        driver.find_element_by_id("submit").click()

        # Editing the lastname of third row
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "edit-record-3")))
        element = driver.find_element_by_id("edit-record-3")
        element.click()
        element = driver.find_element_by_id("lastName")
        element.clear()
        element.send_keys("Malhotra")
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "submit")))
        driver.find_element_by_id("submit").click()

        # Deleting the second row
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "delete-record-2")))
        element = driver.find_element_by_id("delete-record-2")
        element.click()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
