from generic import XLUtils

path = r'C:\Users\Dell\PycharmProjects\Hybrid_Framework\excel_files\locators.xlsx'
locators = XLUtils.read_locators(path, 'loginpage')

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def username_textfield(self, un):
        self.driver.find_element(*locators['email_textfield']).send_keys(un)

    def password_textfield(self, pwd):
        self.driver.find_element(*locators['password_textfield']).send_keys(pwd)

    def login_button(self):
        self.driver.find_element(*locators['login_button']).click()