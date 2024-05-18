from selenium.webdriver.remote.webdriver import WebDriver

from discuz.model.post import Post
from discuz.scraper import Scraper


class BoardPage(Scraper):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def post_board(self, posts: list[Post]):
        for post in posts:
            enter_board_link_path = f"//a[text()='{post.board_name}']"
            enter_board_link = self._wait_find(enter_board_link_path)
            enter_board_link.click()
