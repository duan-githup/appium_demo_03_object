from page.login_page import LoginPage


class Page:
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        return LoginPage(self.driver)