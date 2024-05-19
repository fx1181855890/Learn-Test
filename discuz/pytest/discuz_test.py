from selenium import webdriver

from discuz.page.board_page import BoardPage
from discuz.page.main_page import MainPage
from discuz.util import load_post_data, load_recommend_data

driver = webdriver.Chrome()
main_page = MainPage(driver)
board_page = BoardPage(driver)

# Sign in as admin
main_page.sign_in(username="admin", password="admin")
assert main_page.is_signed_in()

# Load posts from JSON
loaded_posts = load_post_data()
loaded_recommends = load_recommend_data()

# Submit posts
for loaded_post in loaded_posts:
    main_page.init()
    main_page.enter_board(loaded_post.board_name)
    board_page.submit_post(loaded_post)

# Sign in as test user
main_page.sign_out()
main_page.sign_in(username="test", password="123456")

# Recommend posts
for loaded_recommend in loaded_recommends:
    main_page.init()
    main_page.enter_board(loaded_recommend.board_name)
    board_page.recommend_post(loaded_recommend)

driver.quit()
