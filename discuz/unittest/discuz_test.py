from selenium import webdriver

from discuz import Discuz

webdriver = webdriver.Chrome()
discuz = Discuz(webdriver)
discuz.sign_in("admin", "admin")
discuz.init_board()
discuz.add_board(["new board a", "new board b"])

print()
