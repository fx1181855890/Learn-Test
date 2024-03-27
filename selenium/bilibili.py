from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait

from user import *


class Bilibili:
    def __init__(self, webdriver: WebDriver):
        self.driver = webdriver
        self.wait = WebDriverWait(self.driver, timeout=4)
        self.search_input_path = "//input[@class='nav-search-input']"
        self.search_button_path = "//div[@class='nav-search-btn']"
        self.card_div_path = "//div[@class='bili-video-card']"
        self.title_h3_path = ".//h3[@class='bili-video-card__info--tit']"
        self.author_span_path = ".//span[@class='bili-video-card__info--author']"
        self.date_div_path = ".//div[@class='pubdate']"
        self.description_span_path = "//span[@class='desc-info-text']"

    def search(self):
        search_input = self.wait.until(presence_of_element_located((By.XPATH, self.search_input_path)))
        search_input.send_keys("前端")
        search_button = self.wait.until(presence_of_element_located((By.XPATH, self.search_button_path)))
        search_button.click()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def process_cards(self, target_card_count=20):
        users = []
        last_count = 0

        while len(users) < target_card_count:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                self.wait.until(
                    lambda d: len(d.find_elements(By.XPATH, self.card_div_path)) > last_count
                )
            except TimeoutException:
                print("Timed out waiting for more cards to load.")
                break

            card_divs = self.driver.find_elements(By.XPATH, self.card_div_path)
            last_count = len(card_divs)

            for index, card_div in enumerate(card_divs[len(users):target_card_count], start=len(users) + 1):
                try:
                    print(f"Processing card [{index}/{target_card_count}]")
                    user = self.process_card(card_div)
                    users.append(user)
                except Exception as e:
                    print(f"Exception: {e}")
                    break

        save_users_to_csv(users, "users.csv")

    def process_card(self, card_div: WebElement) -> User:
        user = User()
        user.name = card_div.find_element(By.XPATH, self.title_h3_path).text
        user.up = card_div.find_element(By.XPATH, self.author_span_path).text
        try:
            card_div.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            user.pubdate = self.wait.until(presence_of_element_located((By.XPATH, self.date_div_path))).text
            try:
                user.course_desc = self.wait.until(presence_of_element_located((By.XPATH, self.description_span_path))).text
            except Exception:
                user.course_desc = ""
        except Exception as e:
            raise e
        finally:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            return user
