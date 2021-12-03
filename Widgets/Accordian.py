import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Accordion(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/accordian")

    def test_accordion(self):
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='section1Content']/p")
        txt = element.text
        if "scrambled" in txt:
            print("Text shown correctly")
        else:
            print("check where went wrong")
        element = driver.find_element_by_id("section1Heading")
        element.click()
        WebDriverWait(driver, 500).until(expected_conditions.element_to_be_clickable((By.ID, "section2Heading")))
        element = driver.find_element_by_id("section2Heading")
        element.click()
        element = driver.find_element_by_xpath("//*[@id='section2Content']/p[2]")
        txt = element.text
        time.sleep(5)
        if "standard" in txt:
            print("check where went wrong")
        else:
            print("Text shown correctly")
        WebDriverWait(driver, 1500).until(expected_conditions.element_to_be_clickable((By.ID, "section2Heading")))
        element = driver.find_element_by_id("section2Heading")
        element.click()
        WebDriverWait(driver, 1500).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='section3Heading']")))
        element = driver.find_element_by_xpath("//*[@id='section3Heading']")
        element.click()
        time.sleep(5)
        if "infancy" in txt:
            print("check where went wrong")
        else:
            print("Text shown correctly")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
