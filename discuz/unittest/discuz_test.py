from selenium import webdriver

from unittest.model.board import Board
from unittest.page.board_page import BoardPage
from unittest.page.user_page import UserPage

webdriver = webdriver.Chrome()
user_page = UserPage(webdriver)
board_page = BoardPage(webdriver)

user_page.sign_in(username="admin", password="admin")
board_page.init_board()

boards = []
board = Board(order=1, forum="new forum a", inherited="默认版块")
boards.append(board)

board_page.add_boards(boards)

print()
