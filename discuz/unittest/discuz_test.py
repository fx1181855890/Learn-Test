from selenium import webdriver

from discuz import Discuz
from board import Board

webdriver = webdriver.Chrome()
discuz = Discuz(webdriver)

discuz.sign_in("admin", "admin")
discuz.init_board()

boards = []
boards.append(Board(order=0, forum="new forum a", inherited="默认板块"))

discuz.add_boards(boards)

print()
