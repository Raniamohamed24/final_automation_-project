import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestViewPolicyDetails(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.guru99.com/insurance/v1/index.php")

    def test_successfully_view_policy_details(self):
        driver = self.driver
        # Log in to the application
        driver.find_element(By.ID, "email").send_keys("valid_user@example.com")
        driver.find_element(By.ID, "password").send_keys("valid_password")
        driver.find_element(By.NAME, "submit").click()

        # Wait and slow down the process
        time.sleep(2)  # Wait for 2 seconds to allow login to complete

        # Navigate to "View Policy" page
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "View Policy"))
        ).click()

        time.sleep(2)  # Wait for 2 seconds to allow navigation to the page

        # Select the policy from the list
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Policy ID"))  # Replace with actual ID
        ).click()

        time.sleep(2)  # Wait for 2 seconds to allow policy details to load

        # Verify that the correct policy details are displayed
        policy_details = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "policy_details"))
        ).text
        self.assertIn("Policy Details", policy_details)  # Adjust based on actual details

    def tearDown(self):
        self.driver.quit()

class TestViewPolicyDetailsInvalidID(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.guru99.com/insurance/v1/index.php")

    def test_view_policy_details_invalid_id(self):
        driver = self.driver
        # Log in to the application
        driver.find_element(By.ID, "email").send_keys("valid_user@example.com")
        driver.find_element(By.ID, "password").send_keys("valid_password")
        driver.find_element(By.NAME, "submit").click()

        # Wait and slow down the process
        time.sleep(2)  # Wait for 2 seconds to allow login to complete

        # Navigate to "View Policy" page
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "View Policy"))
        ).click()

        time.sleep(2)  # Wait for 2 seconds to allow navigation to the page

        # Enter an invalid policy ID and search
        driver.find_element(By.ID, "policy_id").send_keys("invalid_policy_id")
        driver.find_element(By.NAME, "search").click()

        time.sleep(2)  # Wait for 2 seconds to allow search to complete

        # Verify that an appropriate error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "error_message"))
        ).text
        self.assertIn("Invalid policy ID", error_message)

    def tearDown(self):
        self.driver.quit()

class TestViewPolicyDetailsWithoutLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.guru99.com/insurance/v1/index.php")

    def test_view_policy_details_without_login(self):
        driver = self.driver
        # Navigate to "View Policy" page without logging in
        driver.get("http://demo.guru99.com/insurance/v1/policy.php")

        time.sleep(2)  # Wait for 2 seconds to allow page to load

        # Attempt to view policy details
        driver.find_element(By.ID, "policy_id").send_keys("some_policy_id")
        driver.find_element(By.NAME, "search").click()

        time.sleep(2)  # Wait for 2 seconds to allow search to complete

        # Verify that a login prompt or error message is displayed
        login_prompt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_prompt"))
        ).text
        self.assertIn("Please log in to view policy details", login_prompt)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
