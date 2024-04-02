import traceback

from selenium.webdriver.support.expected_conditions import *

from scrape.scraper import Scraper, get_base_url
from model.up import *
from model.user import *


class Bilibili(Scraper):
    def __init__(self):
        super().__init__("https://search.bilibili.com/all?keyword=%E5%89%8D%E7%AB%AF&order=click")

        self.current_card_index = 0
        self.target_total_card_count = 0

        self.search_input_path = "//input[@class='nav-search-input']"
        self.search_button_path = "//div[@class='nav-search-btn']"
        self.max_played_button_path = "//button[text()='最多播放']"

        self.card_div_path = "//div[@class='bili-video-card']"
        self.close_div_path = "//div[@class='close']"
        self.next_button_path = "//button[text()='下一页']"

        self.title_h3_path = ".//h3[@class='bili-video-card__info--tit']"
        self.author_span_path = ".//span[@class='bili-video-card__info--author']"
        self.cover_img_path = ".//picture[@class='v-img bili-video-card__cover']/img"
        self.up_a_path = ".//a[@class='bili-video-card__info--owner']"

        self.date_div_path = "//div[@class='pubdate-ip-text']"
        self.description_span_path = "//span[@class='desc-info-text']"
        self.like_span_path = "//span[@class='video-like-info video-toolbar-item-text']"
        self.fav_span_path = "//span[@class='video-fav-info video-toolbar-item-text']"
        self.view_div_path = "//div[@class='view-text']"
        self.tag_div_path = "//div[@class='tag not-btn-tag']"

        self.up_desc_h4_path = "//h4[@class='h-sign']"
        self.avatar_img_path = "//div[@class='bili-avatar']/img"

    def search(self):
        search_input = self._wait_find(self.search_input_path)
        search_input.send_keys("前端")
        search_button = self._wait_find(self.search_button_path)
        search_button.click()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def process_cards(self, target_total_card_count=100):
        self.target_total_card_count = target_total_card_count

        users = []
        ups = []

        self._wait_find(self.max_played_button_path).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self._wait_find(self.close_div_path).click()

        try:
            remain_card_count = target_total_card_count
            while remain_card_count > 0:
                target_page_card_count = min(remain_card_count, 24)
                users, ups = self.process_page(users, ups, target_page_card_count)
                remain_card_count -= target_page_card_count

                reference_element = self._wait_find(self.card_div_path)
                self._wait_find(self.next_button_path).click()
                self._wait_for_staleness(reference_element)
        except Exception as e:
            save_users_to_csv(users, "data/users.csv")
            save_ups_to_csv(ups, "data/ups.csv")
            raise e

        save_users_to_csv(users, "data/users.csv")
        save_ups_to_csv(ups, "data/ups.csv")

    def process_page(self, users, ups, target_page_card_count) -> (list[User], list[Up]):
        card_divs = self._wait_find(self.card_div_path, find_all=True)
        for card_div in card_divs[0:target_page_card_count]:
            self.current_card_index += 1
            print(f"Processing card [{self.current_card_index}/{self.target_total_card_count}] ...")
            user, up = self.process_card(card_div)
            users.append(user)
            ups.append(up)
        return users, ups

    def process_card(self, card_div: WebElement) -> (User, Up):
        user = User()

        user.name = self._wait_find(self.title_h3_path, element=card_div).text
        user.up = self._wait_find(self.author_span_path, element=card_div).text
        user.card_url = self._wait_find(self.cover_img_path, element=card_div).get_attribute("src")

        try:
            card_div.click()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            user.url = get_base_url(self.driver.current_url)
            user.pubdate = self._wait_find(self.date_div_path).text
            user.course_like = self._wait_find(self.like_span_path).text
            user.course_fav = self._wait_find(self.fav_span_path).text
            user.course_view = self._wait_find(self.view_div_path).text
            tags = self._wait_find(self.tag_div_path, find_all=True)
            user.tag = [tag.text for tag in tags]
            try:
                user.course_desc = self._wait_find(self.description_span_path).text
            except Exception:
                user.course_desc = ""
        except Exception as e:
            traceback.print_exc()
            raise e
        finally:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        up = Up()

        up_url = self._wait_find(self.up_a_path, element=card_div)
        up.name = self._wait_find(self.author_span_path, element=card_div).text

        try:
            up_url.click()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            up.up_desc = self._wait_find(self.up_desc_h4_path, timeout=10).text
            up.avatar_url = self._wait_find(self.avatar_img_path).get_attribute("src")
        except Exception as e:
            traceback.print_exc()
            raise e
        finally:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        return user, up
