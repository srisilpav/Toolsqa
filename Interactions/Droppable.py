import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By, By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class DropabbleTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/droppable")

    def test_droppabble(self):
        driver = self.driver

        # drag the "Drag me" box to the "Drop here" box and check the text change
        element = driver.find_element_by_xpath("//*[@id='droppable']/p")
        print(element.text)
        element_to_be_dragged = driver.find_element_by_id("draggable")
        element_target = driver.find_element_by_id("droppable")
        action = ActionChains(driver)
        action.click_and_hold(element_to_be_dragged).move_to_element(element_target).release().perform()
        element = driver.find_element_by_xpath("//*[@id='droppable']/p")
        print(element.text)

        # click on the "Accept" tab and drag "Acceptable" and "Not Acceptable" boxes to
        # "Drop here" box to check the acceptability
        element = driver.find_element_by_id("droppableExample-tab-accept")
        element.click()
        element = driver.find_element_by_id("droppable")
        print(element.text)
        element_to_be_dragged = driver.find_element_by_id("notAcceptable")
        print(element_to_be_dragged.is_displayed())
        action = ActionChains(driver)
        action.click_and_hold(element_to_be_dragged).move_by_offset(250, 0).move_by_offset(-250, 0).release().perform()
        element_to_be_dragged = driver.find_element_by_id("acceptable")
        action = ActionChains(driver)
        action.click_and_hold(element_to_be_dragged).move_by_offset(250, 0).release().perform()

        # click on the "Prevent Propogation" tab and drag "Drag Me" box  to
        # "Outer droppable" box ,"Inner droppable(not greedy)box,"Outer droppable"box and "Inner droppable(greedy)boxes
        element = driver.find_element_by_id("droppableExample-tab-preventPropogation")
        element.click()
        element = driver.find_element_by_xpath("//*[@id='notGreedyDropBox']/p")
        print(element.text)
        element_to_be_dragged = driver.find_element_by_id("dragBox")
        element_target = driver.find_element_by_xpath("//*[@id='notGreedyDropBox']/p")
        action = ActionChains(driver)
        action.click_and_hold(element_to_be_dragged).move_to_element(element_target).release().perform()
        element = driver.find_element_by_xpath("//*[@id='notGreedyDropBox']/p")
        element = driver.find_element_by_xpath("//*[@id='notGreedyInnerDropBox']/p")
        element_to_be_dragged = driver.find_element_by_id("dragBox")
        element_target = driver.find_element_by_xpath("//*[@id='notGreedyInnerDropBox']/p")
        action = ActionChains(driver)
        action.click_and_hold(element_to_be_dragged).move_to_element(element_target).release().perform()
        element = driver.find_element_by_xpath("//*[@id='notGreedyInnerDropBox']/p")
        element = driver.find_element_by_xpath("//*[@id='greedyDropBox']/p")
        element = driver.find_element_by_xpath("//*[@id='greedyDropBox']/p")
        element_to_be_dragged = driver.find_element_by_id("dragBox")
        element_target = driver.find_element_by_xpath("//*[@id='greedyDropBox']/p")
        action = ActionChains(driver)
        action.click_and_hold(element_to_be_dragged).move_to_element(element_target).release().perform()
        element = driver.find_element_by_xpath("//*[@id='greedyDropBox']/p")
        element = driver.find_element_by_id("droppableExample-tab-preventPropogation")
        element.click()
        element = driver.find_element_by_xpath("//*[@id='greedyDropBoxInner']/p")
        element_to_be_dragged = driver.find_element_by_id("dragBox")
        element_target = driver.find_element_by_xpath("//*[@id='greedyDropBoxInner']/p")
        action = ActionChains(driver)
        action.click_and_hold(element_to_be_dragged).move_to_element(element_target).release().perform()
        element = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='greedyDropBoxInner']/p")))

        # click on the "Revert Draggable" tab and drag "Will Revert" box  ,
        # "Not Revert" box to "Drop here"box
        element = driver.find_element_by_id("droppableExample-tab-revertable")
        element.click()
        time.sleep(5)
        element_to_be_dragged = WebDriverWait(driver,50).until(expected_conditions.presence_of_element_located((By.ID,"revertable")))
        print(element.is_displayed())
        element_target = WebDriverWait(driver,5).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='droppable']")))
        action = ActionChains(driver)
        action.click_and_hold(element_to_be_dragged).move_by_offset(250, 0).release().perform()
        element_to_be_dragged = driver.find_element_by_id("notRevertable")
        element_target = driver.find_element_by_id("droppable")
        action = ActionChains(driver)
        action.click_and_hold(element_to_be_dragged).move_by_offset(250, 0).move_by_offset(-250, 0).release().perform()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
