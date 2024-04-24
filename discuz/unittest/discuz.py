from selenium.webdriver.remote.webdriver import WebDriver

from scraper import Scraper


class Discuz(Scraper):
    def __init__(self, driver: WebDriver):
        self.base_url = "http://localhost:8080/admin.php?action=forums"
        super().__init__(self.base_url, driver)

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

    def init_board(self):
        self.driver.switch_to.frame(0)

    def add_board(self, board_names: list[str]):
        add_board_a_path = "//div[@class='lastboard']/a"
        add_board_input_path = "(//input[@name='newforum[1][]'])[last()]"

        add_board_a = self._wait_find(add_board_a_path)

        for board_name in board_names:
            add_board_a.click()
            add_board_input = self._wait_find(add_board_input_path)
            add_board_input.clear()
            add_board_input.send_keys(board_name)


