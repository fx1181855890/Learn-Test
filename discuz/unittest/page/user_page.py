from selenium.webdriver.remote.webdriver import WebDriver

from unittest.scraper import Scraper


class UserPage(Scraper):
    def __init__(self, driver: WebDriver):
        self.base_url = "http://localhost:8080/admin.php?action=forums"
        super().__init__(driver, self.base_url)

    def sign_in(self, username: str, password: str):
        username_input_path = "//input[@name='admin_username']"
        password_input_path = "//input[@name='admin_password']"
        submit_input_path = "//input[@name='submit']"

        username_input = self._wait_find(username_input_path)
        username_input.send_keys(username)
        password_input = self._wait_find(password_input_path)
        password_input.send_keys(password)
        submit_input = self._wait_find(submit_input_path)
        submit_input.click()
