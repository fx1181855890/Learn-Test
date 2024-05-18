from selenium import webdriver

from discuz.page.board_page import BoardPage
from discuz.page.main_page import MainPage
from discuz.util import load_post__data_from_json


driver = webdriver.Chrome()
main_page = MainPage(driver)
board_page = BoardPage(driver)

# Sign in
main_page.sign_in(username="admin", password="admin")
assert main_page.is_signed_in()

# Load posts from JSON
loaded_posts = load_post__data_from_json()

for loaded_post in loaded_posts:
    main_page.enter_board(loaded_post.board_name)
    board_page.post_board(loaded_post)

driver.quit()
