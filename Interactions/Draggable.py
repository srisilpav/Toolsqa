import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class DraggableTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/dragabble")

    def test_draggable(self):
        driver = self.driver

        # Drag the "Drag me" button
        element = driver.find_element_by_id("dragBox")
        action = ActionChains(driver)
        action.click_and_hold(element).move_by_offset(95, 0).pause(2).move_by_offset(-80, 0).pause(2).move_by_offset(
            120, 0).perform()

        # click on the "Axis Restricted" tab and drag "Only X" and "Only Y".
        element = driver.find_element_by_id("draggableExample-tab-axisRestriction")
        element.click()
        element = driver.find_element_by_id("restrictedX")
        action = ActionChains(driver)
        action.click_and_hold(element).move_by_offset(65, 0).pause(2).move_by_offset(-80, 0).pause(2).move_by_offset(95,
                                                                                                                     0).perform()
        element = driver.find_element_by_id("restrictedY")
        action = ActionChains(driver)
        action.click_and_hold(element).move_by_offset(0, 75).pause(2).move_by_offset(0, -85).pause(2).move_by_offset(0,
                                                                                                                     105).perform()

        # click on the "Container Restricted" tab  to drag the content boxes
        element = driver.find_element_by_id("draggableExample-tab-containerRestriction")
        element.click()
        element = driver.find_element_by_xpath("//*[@id='containmentWrapper']/div")
        action = ActionChains(driver)
        action.click_and_hold(element).move_by_offset(75, 26).pause(2).move_by_offset(-80, 120).pause(2).move_by_offset(
            150, 50).perform()
        element = driver.find_element_by_xpath("//*[@id='draggableExample-tabpane-containerRestriction']/div[2]/span")
        action = ActionChains(driver)
        action.click_and_hold(element).move_by_offset(10, 15).pause(2).move_by_offset(-10, 10).pause(2).move_by_offset(
            10, 20).perform()

        # click on the "cursor Style" tab and drag all the boxes
        element = driver.find_element_by_id("draggableExample-tab-cursorStyle")
        element.click()
        element = driver.find_element_by_id("cursorCenter")
        action = ActionChains(driver)
        action.click_and_hold(element).move_by_offset(75, 26).pause(2).move_by_offset(-80, 120).pause(2).move_by_offset(
            150, 50).perform()
        element = driver.find_element_by_id("cursorTopLeft")
        action = ActionChains(driver)
        action.click_and_hold(element).move_by_offset(75, 26).pause(2).move_by_offset(-80, 120).pause(2).move_by_offset(
            150, 50).perform()
        element = driver.find_element_by_id("cursorBottom")
        action = ActionChains(driver)
        action.click_and_hold(element).move_by_offset(75, 26).pause(2).move_by_offset(-80, 120).pause(2).move_by_offset(
            150, 50).perform()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
