from selenium.webdriver.remote.webdriver import WebDriver

from scraper import Scraper


class Discuz(Scraper):
    def __init__(self, driver: WebDriver):
        self.base_url = "http://localhost:8080/admin.php?action=forums"
        super().__init__(self.base_url, driver)

        self.username_input_path = "//input[@name='admin_username']"
        self.password_input_path = "//input[@name='admin_password']"
        self.submit_input_path = "//input[@name='submit']"

        self.add_board_a_path = "//div[@class='lastboard']/a"

    def sign_in(self, username: str, password: str):
        username_input = self._wait_find(self.username_input_path)
        username_input.send_keys(username)
        password_input = self._wait_find(self.password_input_path)
        password_input.send_keys(password)
        submit_input = self._wait_find(self.submit_input_path)
        submit_input.click()

    def add_board(self):
        add_board_a = self._wait_find(self.add_board_a_path)
        add_board_a.click()
