from selenium.webdriver.remote.webdriver import WebDriver

from discuz.model.board import Board
from discuz.scraper import Scraper


class BoardPage(Scraper):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

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
            new_inherited_option_path = f".//option[contains(text(), '{board.inherited}')]"
            new_inherited_option = self._wait_find(new_inherited_option_path, new_inherited_select)
            new_inherited_option.click()

        submit_input = self._wait_find(submit_input_path)
        submit_input.click()

    def clean_up(self):
        delete_links_path = "//a[text()='删除']"
        confirm_button_path = "//input[@name='confirmed']"

        while True:
            delete_links = self._wait_find(delete_links_path, find_all=True, timeout=4)
            if len(delete_links) <= 2:
                break

            delete_link = delete_links[-1]
            delete_link.click()
            confirm_button = self._wait_find(confirm_button_path)
            confirm_button.click()
