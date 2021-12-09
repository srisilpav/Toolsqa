import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class UploadDownloadTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/upload-download")

    def test_uploadDownloadTests(self):
        driver = self.driver

        # click on the "Download" button to download the file.
        wait = WebDriverWait(driver, 20)
        element = wait.until(expected_conditions.visibility_of_element_located(
            (By.ID, "downloadButton")))
        element.click()

        # Uploading a file
        element = driver.find_element_by_id("uploadFile")
        element.send_keys("C:\\Users\\vssil\\Apple\\Fuji.JPG")

        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
