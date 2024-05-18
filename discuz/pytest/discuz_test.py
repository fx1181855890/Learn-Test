import unittest
from selenium import webdriver

from discuz.page.board_page import BoardPage
from discuz.page.user_page import UserPage
from discuz.util import load_post__data_from_json


driver = webdriver.Chrome()
user_page = UserPage(driver)
board_page = BoardPage(driver)

# Sign in
user_page.sign_in(username="admin", password="admin")
assert user_page.is_signed_in()

# Load posts from JSON
loaded_posts = load_post__data_from_json()

board_page.post_board(loaded_posts)

driver.quit()
