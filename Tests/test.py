import unittest
import random
import string
import html
import HtmlTestRunner

from random import randint
from selenium import webdriver

class BrickDashboard(unittest.TestCase):
    
    # declare variable to store the URL to be visited
    signup_url = "https://brick-qa-assignment.herokuapp.com/"
    login_url = "https://brick-qa-assignment.herokuapp.com/login"
    
    # declare variable to store search term. This variable can be stored to another file, but for now, this should work.
    signup_first_name="Test"
    signup_last_name="Michael"
    signup_address="Rockbottom"
    login_email="indomie.telur09@gmail.com"
    login_password="Unang1234"
    
    # --- Pre Condition ---
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\Automation\Brick---QA-Engineer-Assessment\webdriver\chromedriver.exe") # please change this exec path following your own folder path
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def email_randomizer(self, length=10, char = string.ascii_lowercase):
        return ''.join(random.choice(char) for i in range(length))
    
    def password_randomizer(self, length=8):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        
        all = lower + upper + num + symbols
        temp = random.sample(all,length)
        a = "".join(temp)
        return '{}'.format(a)
    
    def phone_number_randomizer(self):
        first = str(random.randint(1,99))
        second = str(random.randint(1, 9998)).zfill(4)
        third = (str(random.randint(1, 9998)).zfill(4))
        while third in ['1111','2222','3333','4444','5555','6666', '7777', '8888']:
            third = (str(random.randint(1, 9998)).zfill(4))
        
        return '{}{}{}'.format(first, second, third)
    
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
        email_field.send_keys(self.email_randomizer(),'@gmail.com')
        
        phone_field = self.driver.find_element_by_id('phoneNumber')
        phone_field.send_keys(self.phone_number_randomizer())
        
        address_field = self.driver.find_element_by_id('address')
        address_field.send_keys(self.signup_address)

        a = self.password_randomizer()

        password_field = self.driver.find_element_by_id('password')
        password_field.send_keys(a)
        
        confirm_password_field = self.driver.find_element_by_id('confirm_password')
        confirm_password_field.send_keys(a)
        
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
        self.assertEqual("Welcome Back, Cyborg Rorschach!", login_success_popup.text)
        
    
    # --- Post - Condition (Tear Down) ---
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = "D:\Automation\OneBrick\Report"))
