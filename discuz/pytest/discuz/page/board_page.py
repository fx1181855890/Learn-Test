from selenium.webdriver.remote.webdriver import WebDriver

from discuz.model.post import Post
from discuz.scraper import Scraper


class BoardPage(Scraper):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def post_board(self, post: Post):
        subject_input_path = "//input[@name='subject']"
        message_textarea_path = "//textarea[@name='message']"

        subject_input = self._wait_find(subject_input_path)
        message_input = self._wait_find(message_textarea_path)

        subject_input.send_keys(post.subject)
        message_input.send_keys(post.message)
