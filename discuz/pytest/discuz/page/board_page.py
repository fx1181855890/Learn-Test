from selenium.webdriver.remote.webdriver import WebDriver

from discuz.model.comment import Comment
from discuz.model.post import Post
from discuz.model.recommend import Recommend
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

    def is_posted(self, post: Post) -> bool:
        post_link_path = f"//a[text()='{post.subject}']"
        try:
            self._wait_find(post_link_path)
            return True
        except:
            return False

    def clear_posts(self):
        checkbox_input_path = "//input[@name='moderate[]']"
        try:
            checkbox_inputs = self._wait_find(checkbox_input_path, find_all=True)
            for checkbox in checkbox_inputs:
                checkbox.click()

            delete_link_path = "//a[text()='删除']"
            delete_link = self._wait_find(delete_link_path)
            delete_link.click()

            confirm_span_path = "//span[text()='确定']"
            confirm_span = self._wait_find(confirm_span_path)
            confirm_span.click()
        except:
            return

    def comment_post(self, comment: Comment):
        post_link_path = f"//a[text()='{comment.subject}']"
        post_link = self._wait_find(post_link_path)
        post_link.click()

        message_textarea_path = "//textarea[@name='message']"
        submit_button_path = "//button[@id='fastpostsubmit']"

        message_textarea = self._wait_find(message_textarea_path)
        submit_button = self._wait_find(submit_button_path)

        message_textarea.send_keys(comment.message)
        submit_button.click()

    def is_commented(self, comment: Comment) -> bool:
        if comment.message == "":
            return False

        post_link_path = f"//a[text()='{comment.subject}']"
        post_link = self._wait_find(post_link_path)
        post_link.click()

        comment_td_path = f"//td[contains(text(), '{comment.message}')]"
        try:
            self._wait_find(comment_td_path)
            return True
        except:
            return False

    def recommend_post(self, recommend: Recommend):
        post_link_path = f"//a[text()='{recommend.subject}']"
        post_link = self._wait_find(post_link_path)
        post_link.click()

        recommend_link_path = "//a[@id='recommend_add']"
        recommend_link = self._wait_find(recommend_link_path)
        recommend_link.click()

