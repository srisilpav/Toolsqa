import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LinksTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/links")

    def test_links(self):
        driver = self.driver
        element = driver.find_element_by_id("simpleLink")
        element.click()
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.close()
        driver.switch_to.window(window_before)
        element = driver.find_element_by_id("dynamicLink")
        element.click()
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.close()
        driver.switch_to.window(window_before)
        element = driver.find_element_by_id("created")
        element.click()
        element=driver.find_element_by_xpath("//*[@id='linkResponse']/b[1]")
        self.assertEqual(element.text,"201","value is not same")
        element = driver.find_element_by_id("no-content")
        element.click()
        element = driver.find_element_by_id("moved")
        element.click()
        WebDriverWait(driver,30).until(expected_conditions.element_to_be_clickable((By.ID,"bad-request")))
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "unauthorized")))
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "forbidden")))
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "invalid-url")))




    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
