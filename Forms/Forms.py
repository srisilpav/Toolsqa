import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class FormTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")

    def test_forms(self):
        driver = self.driver
        element = driver.find_element_by_id("firstName")
        element.send_keys("Sri")
        element = driver.find_element_by_id("lastName")
        element.send_keys("Rama")
        element = driver.find_element_by_id("userEmail")
        element.send_keys("srirama@gmail.com")
        element = driver.find_element_by_xpath("//*[@id='genterWrapper']/div[2]/div[1]/label")
        element.click()
        element = driver.find_element_by_id("userNumber")
        element.send_keys("5556655566")
        time.sleep(5)
        element = WebDriverWait(driver, 150).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]")))
        element.click()
        element = driver.find_element_by_xpath("//*[@id='hobbiesWrapper']/div[2]/div[3]")
        element.click()

        element = WebDriverWait(driver, 30).until(
            expected_conditions.element_to_be_clickable((By.ID, "uploadPicture")))
        element.send_keys("C:\\Users\\vssil\\Apple\\Fuji.JPG")
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.ID, "currentAddress")))
        element.send_keys("012345 Seshu Seyana complex, vaikunta")
        element = WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='userForm']/div[11]/div")))
        element.click()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
