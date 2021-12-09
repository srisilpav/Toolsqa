import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MenuTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/menu#")

    def test_menu(self):
        driver = self.driver

        # click on all the menu items
        element = driver.find_element_by_xpath("//*[@id='nav']/li[1]/a")
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='nav']/li[1]/a")))
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element_by_xpath("//*[@id='nav']/li[2]/a")
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='nav']/li[2]/a")))
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element_by_xpath("//*[@id='nav']/li[2]/ul/li[1]/a")
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='nav']/li[2]/ul/li[1]/a")))
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element_by_xpath("//*[@id='nav']/li[2]/ul/li[2]/a")
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='nav']/li[2]/ul/li[2]/a")))
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element_by_xpath("//*[@id='nav']/li[2]/ul/li[3]/a")
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/a")))
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element_by_xpath("//*[@id='nav']/li[2]/ul/li[3]/ul/li[1]/a")
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/ul/li[1]/a")))
        action = ActionChains(driver)
        action.move_to_element(element).perform()

        element = driver.find_element_by_xpath("//*[@id='nav']/li[2]/ul/li[3]/ul/li[2]/a")
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/ul/li[2]/a")))
        action = ActionChains(driver)

        action.move_to_element(element).perform()

        element = driver.find_element_by_xpath("//*[@id='nav']/li[3]/a")
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='nav']/li[3]/a")))
        action = ActionChains(driver)
        action.move_to_element(element).perform()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
