import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SelectTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/selectable")

    def test_select(self):
        driver = self.driver

        # Select and de-select the list items.
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='verticalListContainer']/li[1]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='verticalListContainer']/li[2]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='verticalListContainer']/li[3]")))
        element.click()
        time.sleep(5)
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='verticalListContainer']/li[1]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='verticalListContainer']/li[2]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='verticalListContainer']/li[3]")))
        element.click()

        # click on the "Grid" tab to select and de-select the boxes
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.ID, "demo-tab-grid")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row1']/li[1]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row1']/li[2]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row1']/li[3]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row2']/li[1]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row2']/li[2]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row2']/li[3]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row1']/li[1]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row1']/li[2]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row1']/li[3]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row2']/li[1]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row2']/li[2]")))
        element.click()
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='row2']/li[3]")))
        element.click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
