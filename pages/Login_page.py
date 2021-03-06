from pages.Base_page import BasePage
from locators.Login_page_locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):

    login_url = BasePage.main_url + '/admin/login/?next=/admin/'

    def open_login_page(self):
        self.open(self.login_url)

    def get_username_field(self):
        field = self.find_element(self.USERNAME)
        return field

    def fill_username_field(self, username):
        field = self.get_username_field()
        field.send_keys(username)
        return field

    def get_password_field(self):
        field = self.find_element(self.PASSWORD)
        return field

    def fill_password_field(self, password):
        field = self.get_password_field()
        field.send_keys(password)
        return field

    def get_login_field(self):
        field = self.find_element(self.LOG_IN)
        return field

    def click_login_field(self):
        field = self.get_login_field()
        field.click()
        return field

    def login(self, username, password):
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.click_login_field()
