from selenium import webdriver

from unittest.page.board_page import BoardPage
from unittest.page.user_page import UserPage
from unittest.util import load_boards_from_json

# Initialize WebDriver
webdriver = webdriver.Chrome()

# Sign in
user_page = UserPage(webdriver)
user_page.sign_in(username="admin", password="admin")

# Initialize board page
board_page = BoardPage(webdriver)
board_page.init_board()

# Load boards from JSON
loaded_boards = load_boards_from_json()

# Add boards using the board page
board_page.add_boards(loaded_boards)

print("Boards have been added.")
