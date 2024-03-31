import traceback

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait

from scraper import Scraper, get_base_url
from user import *


class Bilibili(Scraper):
    def __init__(self, webdriver: WebDriver):
        super().__init__(webdriver)

        self.url = "https://search.bilibili.com/all?keyword=%E5%89%8D%E7%AB%AF&order=click"

        self.search_input_path = "//input[@class='nav-search-input']"
        self.search_button_path = "//div[@class='nav-search-btn']"
        self.max_played_button_path = "//button[text()='最多播放']"

        self.card_div_path = "//div[@class='bili-video-card']"
        self.close_div_path = "//div[@class='close']"
        self.title_h3_path = ".//h3[@class='bili-video-card__info--tit']"
        self.author_span_path = ".//span[@class='bili-video-card__info--author']"
        self.cover_img_path = ".//picture[@class='v-img bili-video-card__cover']/img"

        self.date_div_path = "//div[@class='pubdate-ip-text']"
        self.description_span_path = "//span[@class='desc-info-text']"
        self.like_span_path = "//span[@class='video-like-info video-toolbar-item-text']"
        self.fav_span_path = "//span[@class='video-fav-info video-toolbar-item-text']"
        self.view_div_path = "//div[@class='view-text']"
        self.tag_div_path = "//div[@class='tag not-btn-tag']"

    def __wait(self, element: WebDriver | WebElement = None) -> WebDriverWait:
        if element is None:
            element = self.driver
        return WebDriverWait(element, timeout=4)

    def __wait_find(self, path: str, element: WebDriver | WebElement = None, find_all=False) -> WebElement | list[WebElement]:
        if element is None:
            element = self.driver
        if find_all is False:
            return self.__wait(element).until(presence_of_element_located((By.XPATH, path)))
        if find_all is True:
            return self.__wait(element).until(presence_of_all_elements_located((By.XPATH, path)))

    def search(self):
        search_input = self.__wait_find(self.search_input_path)
        search_input.send_keys("前端")
        search_button = self.__wait_find(self.search_button_path)
        search_button.click()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def process_cards(self, target_card_count=4):
        users = []
        last_count = 0

        self.__wait_find(self.max_played_button_path).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.__wait_find(self.close_div_path).click()
        self.driver.execute_script("window.scrollTo(0, 0);")

        while len(users) < target_card_count:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                self.__wait().until(
                    lambda d: len(d.find_elements(By.XPATH, self.card_div_path)) > last_count
                )
            except TimeoutException:
                print("Timed out waiting for more cards to load.")
                break

            card_divs = self.__wait_find(self.card_div_path, find_all=True)
            last_count = len(card_divs)

            try:
                for index, card_div in enumerate(card_divs[len(users):target_card_count], start=len(users) + 1):
                    print(f"Processing card [{index}/{target_card_count}]")
                    card_div = self.__wait_find(self.card_div_path, find_all=True)[index]
                    user = self.process_card(card_div)
                    users.append(user)
            except Exception as e:
                save_users_to_csv(users, "users.csv")
                raise e

        save_users_to_csv(users, "users.csv")

    def process_card(self, card_div: WebElement) -> User:
        user = User()
        user.name = self.__wait_find(self.title_h3_path, element=card_div).text
        user.up = self.__wait_find(self.author_span_path, element=card_div).text
        user.card_url = self.__wait_find(self.cover_img_path, element=card_div).get_attribute("src")

        try:
            card_div.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            user.url = get_base_url(self.driver.current_url)
            user.pubdate = self.__wait_find(self.date_div_path).text
            user.course_like = self.__wait_find(self.like_span_path).text
            user.course_fav = self.__wait_find(self.fav_span_path).text
            user.course_view = self.__wait_find(self.view_div_path).text
            tags = self.__wait_find(self.tag_div_path, find_all=True)
            user.tag = [tag.text for tag in tags]
            try:
                user.course_desc = self.__wait_find(self.description_span_path).text
            except Exception:
                user.course_desc = ""
        except Exception as e:
            traceback.print_exc()
            raise e
        finally:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            return user
