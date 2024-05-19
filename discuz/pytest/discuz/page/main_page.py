from selenium.webdriver.remote.webdriver import WebDriver

from discuz.scraper import Scraper


class MainPage(Scraper):
    def __init__(self, driver: WebDriver):
        self.base_url = "http://localhost:8080/index.php"
        super().__init__(driver, self.base_url)

    def init(self):
        self.driver.get(self.base_url)

    def sign_in(self, username: str, password: str):
        username_input_path = "//input[@name='username']"
        password_input_path = "//input[@name='password']"
        submit_button_path = "//button[@type='submit']"

        username_input = self._wait_find(username_input_path)
        username_input.send_keys(username)
        password_input = self._wait_find(password_input_path)
        password_input.send_keys(password)
        submit_input = self._wait_find(submit_button_path)
        submit_input.click()

    def is_signed_in(self) -> bool:
        sign_out_link_path = "//a[text()='退出']"
        sign_out_link = self._wait_find(sign_out_link_path, timeout=5)
        return sign_out_link is not None

    def enter_board(self, board_name: str):
        enter_board_link_path = f"//a[text()='{board_name}']"
        enter_board_link = self._wait_find(enter_board_link_path)
        enter_board_link.click()
