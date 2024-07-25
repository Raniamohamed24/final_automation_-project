import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPolicyApplication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.guru99.com/insurance/v1/index.php")

    def test_successful_policy_application(self):
        driver = self.driver
        # Log in to the application
        driver.find_element(By.ID, "email").send_keys("valid_user@example.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("valid_password")
        time.sleep(1)
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)

        # Navigate to "Apply for Policy" page
        driver.find_element(By.LINK_TEXT, "Apply for Policy").click()
        time.sleep(2)

        # Enter valid details and submit
        driver.find_element(By.ID, "input_field_1").send_keys("Valid Data 1")
        driver.find_element(By.ID, "input_field_2").send_keys("Valid Data 2")
        # ... (fill in all required fields with valid data)
        time.sleep(1)
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)

        # Verify confirmation message
        confirmation_message = driver.find_element(By.ID, "confirmation_message").text
        self.assertIn("Policy successfully applied", confirmation_message)

    def tearDown(self):
        self.driver.quit()


class TestPolicyApplicationMissingFields(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.guru99.com/insurance/v1/index.php")

    def test_policy_application_missing_fields(self):
        driver = self.driver
        # Log in to the application
        driver.find_element(By.ID, "email").send_keys("valid_user@example.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("valid_password")
        time.sleep(1)
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)

        # Navigate to "Apply for Policy" page
        driver.find_element(By.LINK_TEXT, "Apply for Policy").click()
        time.sleep(2)

        # Leave required fields empty and submit
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)

        # Verify error message
        error_message = driver.find_element(By.ID, "error_message").text
        self.assertIn("This field is required", error_message)

    def tearDown(self):
        self.driver.quit()


class TestPolicyApplicationInvalidData(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.guru99.com/insurance/v1/index.php")

    def test_policy_application_invalid_data(self):
        driver = self.driver
        # Log in to the application
        driver.find_element(By.ID, "email").send_keys("valid_user@example.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("valid_password")
        time.sleep(1)
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)

        # Navigate to "Apply for Policy" page
        driver.find_element(By.LINK_TEXT, "Apply for Policy").click()
        time.sleep(2)

        # Enter invalid data and submit
        driver.find_element(By.ID, "input_field_1").send_keys("Invalid Data 1")
        driver.find_element(By.ID, "input_field_2").send_keys("Invalid Data 2")
        # ... (fill in other fields with invalid data, e.g., age below minimum limit)
        time.sleep(1)
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)

        # Verify error message
        error_message = driver.find_element(By.ID, "error_message").text
        self.assertIn("Invalid data", error_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
