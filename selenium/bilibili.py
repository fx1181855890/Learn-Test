from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait

from user import User


class Bilibili:
    def __init__(self, webdriver: WebDriver):
        self.driver = webdriver
        self.wait = WebDriverWait(self.driver, timeout=4)
        self.search_input_path = "//input[@class='nav-search-input']"
        self.search_button_path = "//div[@class='nav-search-btn']"
        self.card_div_path = "//div[@class='bili-video-card']"

    def search(self):
        search_input = self.wait.until(presence_of_element_located((By.XPATH, self.search_input_path)))
        search_input.send_keys("前端")
        search_button = self.wait.until(presence_of_element_located((By.XPATH, self.search_button_path)))
        search_button.click()

    def process_card(self):
        card_divs = self.wait.until(presence_of_all_elements_located((By.XPATH, self.card_div_path)))
        users = []
        for card_div in card_divs:
            user = User()
            users.append(user)
            try:
                user.name = card_div.find_element(By.XPATH, ".//h3[@class='bili-video-card__info--tit']").text
                user.up = card_div.find_element(By.XPATH, ".//span[@class='bili-video-card__info--author']").text
                user.pubdate = card_div.find_element(By.XPATH, ".//span[@class='bili-video-card__info--date']").text
                card_div.click()
                self.driver.switch_to.window(self.driver.window_handles[2])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[1])
            except Exception as e:
                print(e)
                break

        for user in users:
            print(user.name, user.up, user.pubdate)
