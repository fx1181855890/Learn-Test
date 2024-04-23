from selenium import webdriver

from discuz import Discuz

webdriver = webdriver.Chrome()
discuz = Discuz(webdriver)
discuz.sign_in("admin", "admin")
discuz.add_board()
print()
