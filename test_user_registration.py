import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH
        self.driver.get("https://demo.guru99.com/insurance/v1/index.php")  # Replace with the actual URL
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def slow_type(self, element, text):
        for character in text:
            element.send_keys(character)
            time.sleep(0.1)  # Add a small delay between each character

    def test_successful_registration(self):
        # Navigate to the registration page
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
        time.sleep(1)

        # Fill in the registration form
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_firstname"))), "John")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_surname"))), "Doe")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_phone"))), "1234567890")

        Select(self.wait.until(EC.presence_of_element_located((By.ID, "user_dateofbirth_1i")))).select_by_visible_text(
            "1990")
        time.sleep(0.5)
        Select(self.wait.until(EC.presence_of_element_located((By.ID, "user_dateofbirth_2i")))).select_by_visible_text(
            "January")
        time.sleep(0.5)
        Select(self.wait.until(EC.presence_of_element_located((By.ID, "user_dateofbirth_3i")))).select_by_visible_text(
            "1")
        time.sleep(0.5)

        self.wait.until(EC.element_to_be_clickable((By.ID, "licencetype_f"))).click()
        time.sleep(0.5)

        Select(self.wait.until(EC.presence_of_element_located((By.ID, "user_licenceperiod")))).select_by_visible_text(
            "5")
        time.sleep(0.5)
        Select(self.wait.until(EC.presence_of_element_located((By.ID, "user_occupation_id")))).select_by_visible_text(
            "Student")
        time.sleep(0.5)

        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_address_attributes_street"))),
                       "123 Main St")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_address_attributes_city"))),
                       "Anytown")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_address_attributes_county"))),
                       "State")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_address_attributes_postcode"))),
                       "12345")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_user_detail_attributes_email"))),
                       "john.doe@example.com")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_user_detail_attributes_password"))),
                       "password123")
        self.slow_type(self.wait.until(
            EC.presence_of_element_located((By.ID, "user_user_detail_attributes_password_confirmation"))),
                       "password123")

        # Submit the form
        self.wait.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()

        # Verify success message
        success_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.content h3")))
        self.assertEqual(success_message.text, "You have successfully registered")

    def slow_type(self, element, text):
        for character in text:
            element.send_keys(character)
            time.sleep(0.1)  # Add a small delay between each character

    def test_registration_missing_fields(self):
        # Navigate to the registration page
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
        time.sleep(1)

        # Submit the form without filling any fields
        self.wait.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
        time.sleep(2)  # Wait for error messages to appear

        # Verify error messages
        error_messages = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.error_message")))
        self.assertGreater(len(error_messages), 0)

        # Print error messages (optional, for visibility)
        for message in error_messages:
            print(message.text)
            time.sleep(0.5)

    def test_registration_invalid_email(self):
        # Navigate to the registration page
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
        time.sleep(1)

        # Fill in the form with an invalid email
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_user_detail_attributes_email"))),
                       "invalid_email")

        # Fill other required fields
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_firstname"))), "John")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_surname"))), "Doe")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_phone"))), "1234567890")

        Select(self.wait.until(EC.presence_of_element_located((By.ID, "user_dateofbirth_1i")))).select_by_visible_text(
            "1990")
        time.sleep(0.5)
        Select(self.wait.until(EC.presence_of_element_located((By.ID, "user_dateofbirth_2i")))).select_by_visible_text(
            "January")
        time.sleep(0.5)
        Select(self.wait.until(EC.presence_of_element_located((By.ID, "user_dateofbirth_3i")))).select_by_visible_text(
            "1")
        time.sleep(0.5)

        self.wait.until(EC.element_to_be_clickable((By.ID, "licencetype_f"))).click()
        time.sleep(0.5)

        Select(self.wait.until(EC.presence_of_element_located((By.ID, "user_licenceperiod")))).select_by_visible_text(
            "5")
        time.sleep(0.5)
        Select(self.wait.until(EC.presence_of_element_located((By.ID, "user_occupation_id")))).select_by_visible_text(
            "Student")
        time.sleep(0.5)

        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_address_attributes_street"))),
                       "123 Main St")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_address_attributes_city"))),
                       "Anytown")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_address_attributes_county"))),
                       "State")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_address_attributes_postcode"))),
                       "12345")
        self.slow_type(self.wait.until(EC.presence_of_element_located((By.ID, "user_user_detail_attributes_password"))),
                       "password123")
        self.slow_type(self.wait.until(
            EC.presence_of_element_located((By.ID, "user_user_detail_attributes_password_confirmation"))),
                       "password123")

        # Submit the form
        self.wait.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
        time.sleep(2)  # Wait for error message to appear

        # Verify error message for invalid email
        error_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.error_message")))
        self.assertIn("email", error_message.text.lower())

        # Print error message (optional, for visibility)
        print(error_message.text)
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()