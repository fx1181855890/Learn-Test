from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from unittest.scraper import Scraper
from unittest.model.board import Board


class BoardPage(Scraper):
    def __init__(self, driver: WebDriver):
        self.base_url = "http://localhost:8080/admin.php?action=forums"
        super().__init__(self.base_url, driver)

    def init_board(self):
        self.driver.switch_to.frame(0)

    def add_boards(self, boards: list[Board]):
        add_board_a_path = "//div[@class='lastboard']/a"

        new_order_input_path = "(//input[@name='neworder[1][]'])[last()]"
        new_forum_input_path = "(//input[@name='newforum[1][]'])[last()]"
        new_inherited_select_path = "(//select[@name='newinherited[1][]'])[last()]"

        submit_input_path = "//input[@name='editsubmit']"

        add_board_a = self._wait_find(add_board_a_path)

        for board in boards:
            add_board_a.click()

            new_order_input = self._wait_find(new_order_input_path)
            new_forum_input = self._wait_find(new_forum_input_path)
            new_inherited_select = self._wait_find(new_inherited_select_path)

            new_order_input.clear()
            new_order_input.send_keys(str(board.order))

            new_forum_input.clear()
            new_forum_input.send_keys(board.forum)

            new_inherited_select.click()
            new_inherited_option_path = f"(//option[text()='{board.inherited}'])"
            new_inherited_option = self._wait_find(new_inherited_option_path, new_inherited_select)
            new_inherited_option.click()

        submit_input = self._wait_find(submit_input_path)
        # submit_input.click()
