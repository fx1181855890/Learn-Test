from selenium import webdriver

from discuz import process, util
from discuz.page.board_page import BoardPage
from discuz.page.main_page import MainPage

driver = webdriver.Chrome()
main_page = MainPage(driver)
board_page = BoardPage(driver)

# Sign in as admin
main_page.sign_in(username="admin", password="admin")
assert main_page.is_signed_in()

# Load posts from JSON
loaded_posts = util.load_post_data()
loaded_recommends = util.load_recommend_data()
loaded_comments = util.load_comment_data()

# Submit posts
process.submit_posts(main_page, board_page, loaded_posts)

# Sign in as test user
main_page.sign_out()
main_page.sign_in(username="test", password="123456")
assert main_page.is_signed_in()

# Recommend posts
process.recommend_posts(main_page, board_page, loaded_recommends)

# Comment posts
process.comment_posts(main_page, board_page, loaded_comments)

# Sign in as admin
main_page.sign_out()
main_page.sign_in(username="admin", password="admin")
assert main_page.is_signed_in()

# Collect all unique board names from posts
board_names = set(post.board_name for post in loaded_posts)

# Clear posts from all boards
for board_name in board_names:
    main_page.init()
    main_page.enter_board(board_name)
    board_page.clear_posts()

driver.quit()
