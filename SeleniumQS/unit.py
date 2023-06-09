import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    def test_login(self):
        userNameField = self.driver.find_element(By.ID, "ap_email")
        userNameField.clear()
        userNameField.send_keys("son05son28@gmail.com")
        contiunueButton = self.driver.find_element(By.ID, "continue")
        contiunueButton.click()

        passwordField = self.driver.find_element(By.ID, "ap_password")
        passwordField.clear()
        passwordField.send_keys("Sona12345")
        signInButton = self.driver.find_element(By.ID, "signInSubmit")
        time.sleep(5)
        signInButton.click()
        time.sleep(20)

        greetingElement = self.driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
        greetingText = greetingElement.text

        assert greetingText == "Hello, Sona"
        assert self.driver.title == "Amazon.com. Spend less. Smile more."

    def tearDown(self):
        self.driver.close()




