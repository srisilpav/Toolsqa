import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ImagesTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/broken")

    def test_imageTests(self):
        driver = self.driver

        # Check "Tools QA" image is displayed or not
        wait = WebDriverWait(driver, 20)
        element = wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[1]/img[1]")))
        size = element.size
        print(size)
        if size["width"] == 347:
            print("Image is displayed")
        else:
            print("Image is broken")

            # Check broken image is displayed or not
        wait = WebDriverWait(driver, 20)
        element = wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[1]/img[2]")))
        size = element.size
        print(size)
        if size["width"] == 16:
            print("Image is broken")
        else:
            print("Image is displayed")

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
