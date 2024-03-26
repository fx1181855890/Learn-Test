from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait


class Bilibili:
    def __init__(self, webdriver):
        self.driver = webdriver
        self.wait = WebDriverWait(self.driver, timeout=4)
        self.search_input_path = "//input[@placeholder='搜索']"

    def search(self):
        search_input = self.wait.until(presence_of_element_located((By.XPATH, self.search_input_path)))
        search_input.send_keys("前端")
