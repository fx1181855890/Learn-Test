from selenium.webdriver.remote.webdriver import WebDriver

from discuz.model.comment import Comment
from discuz.model.post import Post
from discuz.scraper import Scraper


class BoardPage(Scraper):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def submit_post(self, post: Post):
        subject_input_path = "//input[@name='subject']"
        message_textarea_path = "//textarea[@name='message']"
        submit_button_path = "//button[@value='topicsubmit']"

        subject_input = self._wait_find(subject_input_path)
        message_input = self._wait_find(message_textarea_path)
        submit_button = self._wait_find(submit_button_path)

        subject_input.send_keys(post.subject)
        message_input.send_keys(post.message)
        submit_button.click()

        try:
            self._wait_for_staleness(submit_button)
        except:
            pass

    def recommend_post(self, post: Post):
        post_link_path = f"//a[text()='{post.subject}']"
        post_link = self._wait_find(post_link_path)
        post_link.click()

        recommend_link_path = "//a[@id='recommend_add']"
        recommend_link = self._wait_find(recommend_link_path)
        recommend_link.click()

    def comment_post(self, comment: Comment):
        post_link_path = f"//a[text()='{comment.subject}']"
        post_link = self._wait_find(post_link_path)
        post_link.click()

        message_textarea_path = "//textarea[@name='message']"
        message_textarea = self._wait_find(message_textarea_path)
        message_textarea.send_keys(comment.message)
