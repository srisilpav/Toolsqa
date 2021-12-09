import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SortableTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/sortable")

    def test_sortable(self):
        driver = self.driver

        # sort the elements in the list
        element_start= driver.find_element_by_xpath("//*[@id='demo-tabpane-list']/div/div[1]")
        element_target=driver.find_element_by_xpath("//*[@id='demo-tabpane-list']/div/div[4]")
        actions = ActionChains(driver)
        actions.click_and_hold(element_start).move_to_element(element_target).release().perform()
        element_start = driver.find_element_by_xpath("//*[@id='demo-tabpane-list']/div/div[2]")
        element_target = driver.find_element_by_xpath("//*[@id='demo-tabpane-list']/div/div[6]")
        actions = ActionChains(driver)
        actions.click_and_hold(element_start).move_to_element(element_target).release().perform()
        element_start = driver.find_element_by_xpath("//*[@id='demo-tabpane-list']/div/div[3]")
        element_target = driver.find_element_by_xpath("//*[@id='demo-tabpane-list']/div/div[1]")
        actions = ActionChains(driver)
        actions.click_and_hold(element_start).move_to_element(element_target).release().perform()
        element_start = driver.find_element_by_xpath("//*[@id='demo-tabpane-list']/div/div[5]")
        element_target = driver.find_element_by_xpath("//*[@id='demo-tabpane-list']/div/div[2]")
        actions = ActionChains(driver)
        actions.click_and_hold(element_start).move_to_element(element_target).release().perform()

        # sort the elements in the grid
        element = driver.find_element_by_id("demo-tab-grid")
        element.click()
        element_start = driver.find_element_by_xpath("//*[@id='demo-tabpane-grid']/div/div/div[1]")
        element_target = driver.find_element_by_xpath("//*[@id='demo-tabpane-grid']/div/div/div[5]")
        actions = ActionChains(driver)
        actions.click_and_hold(element_start).move_to_element(element_target).release().perform()
        element_start = driver.find_element_by_xpath("//*[@id='demo-tabpane-grid']/div/div/div[2]")
        element_target = driver.find_element_by_xpath("//*[@id='demo-tabpane-grid']/div/div/div[4]")
        actions = ActionChains(driver)
        actions.click_and_hold(element_start).move_to_element(element_target).release().perform()
        element_start = driver.find_element_by_xpath("//*[@id='demo-tabpane-grid']/div/div/div[5]")
        element_target = driver.find_element_by_xpath("//*[@id='demo-tabpane-grid']/div/div/div[3]")
        actions = ActionChains(driver)
        actions.click_and_hold(element_start).move_to_element(element_target).release().perform()
        element_start = driver.find_element_by_xpath("//*[@id='demo-tabpane-grid']/div/div/div[3]")
        element_target = driver.find_element_by_xpath("//*[@id='demo-tabpane-grid']/div/div/div[6]")
        actions = ActionChains(driver)
        actions.click_and_hold(element_start).move_to_element(element_target).release().perform()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
