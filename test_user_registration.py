import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH
        self.driver.get("https://demo.guru99.com/insurance/v1/index.php")  # Replace with the actual URL
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_successful_registration(self):
        # Navigate to the registration page
        self.driver.find_element(By.LINK_TEXT, "Register").click()

        # Fill in the registration form
        self.driver.find_element(By.ID, "user_firstname").send_keys("John")
        self.driver.find_element(By.ID, "user_surname").send_keys("Doe")
        self.driver.find_element(By.ID, "user_phone").send_keys("1234567890")
        self.driver.find_element(By.ID, "user_dateofbirth_1i").send_keys("1990")
        self.driver.find_element(By.ID, "user_dateofbirth_2i").send_keys("January")
        self.driver.find_element(By.ID, "user_dateofbirth_3i").send_keys("1")
        self.driver.find_element(By.ID, "licencetype_f").click()
        self.driver.find_element(By.ID, "user_licenceperiod").send_keys("5")
        self.driver.find_element(By.ID, "user_occupation_id").send_keys("Student")
        self.driver.find_element(By.ID, "user_address_attributes_street").send_keys("123 Main St")
        self.driver.find_element(By.ID, "user_address_attributes_city").send_keys("Anytown")
        self.driver.find_element(By.ID, "user_address_attributes_county").send_keys("State")
        self.driver.find_element(By.ID, "user_address_attributes_postcode").send_keys("12345")
        self.driver.find_element(By.ID, "user_user_detail_attributes_email").send_keys("john.doe@example.com")
        self.driver.find_element(By.ID, "user_user_detail_attributes_password").send_keys("password123")
        self.driver.find_element(By.ID, "user_user_detail_attributes_password_confirmation").send_keys("password123")

        # Submit the form
        self.driver.find_element(By.NAME, "submit").click()

        # Verify success message
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.content h3"))
        )
        self.assertEqual(success_message.text, "You have successfully registered")

    def test_registration_missing_fields(self):
        # Navigate to the registration page
        self.driver.find_element(By.LINK_TEXT, "Register").click()

        # Submit the form without filling any fields
        self.driver.find_element(By.NAME, "submit").click()

        # Verify error messages
        error_messages = self.driver.find_elements(By.CSS_SELECTOR, "div.error_message")
        self.assertGreater(len(error_messages), 0)

    def test_registration_invalid_email(self):
        # Navigate to the registration page
        self.driver.find_element(By.LINK_TEXT, "Register").click()

        # Fill in the form with an invalid email
        self.driver.find_element(By.ID, "user_user_detail_attributes_email").send_keys("invalid_email")

        # Fill other required fields (simplified for brevity)
        self.driver.find_element(By.ID, "user_firstname").send_keys("John")
        self.driver.find_element(By.ID, "user_surname").send_keys("Doe")
        self.driver.find_element(By.ID, "user_phone").send_keys("1234567890")
        self.driver.find_element(By.ID, "user_dateofbirth_1i").send_keys("1990")
        self.driver.find_element(By.ID, "user_dateofbirth_2i").send_keys("January")
        self.driver.find_element(By.ID, "user_dateofbirth_3i").send_keys("1")
        self.driver.find_element(By.ID, "licencetype_f").click()
        self.driver.find_element(By.ID, "user_licenceperiod").send_keys("5")
        self.driver.find_element(By.ID, "user_occupation_id").send_keys("Student")
        self.driver.find_element(By.ID, "user_address_attributes_street").send_keys("123 Main St")
        self.driver.find_element(By.ID, "user_address_attributes_city").send_keys("Anytown")
        self.driver.find_element(By.ID, "user_address_attributes_county").send_keys("State")
        self.driver.find_element(By.ID, "user_address_attributes_postcode").send_keys("12345")
        self.driver.find_element(By.ID, "user_user_detail_attributes_password").send_keys("password123")
        self.driver.find_element(By.ID, "user_user_detail_attributes_password_confirmation").send_keys("password123")

        # Submit the form
        self.driver.find_element(By.NAME, "submit").click()

        # Verify error message for invalid email
        error_message = self.driver.find_element(By.CSS_SELECTOR, "div.error_message")
        self.assertIn("email", error_message.text.lower())

if __name__ == "__main__":
    unittest.main()
