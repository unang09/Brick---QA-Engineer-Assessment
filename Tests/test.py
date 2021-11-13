import unittest
import random
import string
import html
import HtmlTestRunner

from selenium import webdriver

class BrickDashboard(unittest.TestCase):
    
    # declare variable to store the URL to be visited
    signup_url = "https://brick-qa-assignment.herokuapp.com/"
    login_url = "https://brick-qa-assignment.herokuapp.com/login"
    
    # declare variable to store search term. This variable can be stored to another file, but for now, this should work.
    signup_first_name="Test"
    signup_last_name="Michael"
    signup_email_address="test20qa@gmail.com"
    signup_phone_number="82218777879"
    signup_address="Rockbottom"
    signup_password="Test1234"
    signup_confirm_password="Test1234"
    login_email="indomie.telur09@gmail.com"
    login_password="Unang1234"
    
    # --- Pre Condition ---
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\Automation\OneBrick\webdriver\chromedriver.exe") # please change this exec path following your own folder path
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # --- Steps ---
    def test_register_account(self):
        driver=self.driver
        driver.get(self.signup_url)
        self.assertIn("Brick Sign Up Form",driver.title)
        
        firstName_field = self.driver.find_element_by_id('firstName')
        firstName_field.send_keys(self.signup_first_name)

        lastname_field = self.driver.find_element_by_id('lastName')
        lastname_field.send_keys(self.signup_last_name)
        
        email_field = self.driver.find_element_by_id('email')
        email_field.send_keys(self.signup_email_address)
        
        phone_field = self.driver.find_element_by_id('phoneNumber')
        phone_field.send_keys(self.signup_phone_number)
        
        address_field = self.driver.find_element_by_id('address')
        address_field.send_keys(self.signup_address)
        
        password_field = self.driver.find_element_by_id('password')
        password_field.send_keys(self.signup_password)
        
        confirm_password_field = self.driver.find_element_by_id('confirm_password')
        confirm_password_field.send_keys(self.signup_confirm_password)
        
        register_button = self.driver.find_element_by_css_selector('#myform > div.form-row-last > input')
        register_button.click()
        
        signup_success_popup = self.driver.find_element_by_id("swal2-content")
        self.assertTrue(signup_success_popup.is_displayed())
        self.assertEqual("Check your email to confirm your registration", signup_success_popup.text)
        
    def test_login_account(self):
        driver=self.driver
        driver.get(self.login_url)
        self.assertIn("Login",driver.title)
        
        email_field = self.driver.find_element_by_id("your_email")
        email_field.send_keys(self.login_email)
        
        password_field = self.driver.find_element_by_id("password")
        password_field.send_keys(self.login_password)
        
        login_button = self.driver.find_element_by_css_selector("#myform > div.form-row-last > input")
        login_button.click()
        
        login_success_popup = self.driver.find_element_by_id("swal2-content")
        self.assertTrue(login_success_popup.is_displayed())
        self.assertEqual("Welcome Back, Captain Amazo!", login_success_popup.text)
        
    
    # --- Post - Condition (Tear Down) ---
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = "D:\Automation\OneBrick\Report"))
