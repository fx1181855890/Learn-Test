from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import *

from scraper import Scraper


class Baidu(Scraper):
    def __init__(self, driver: WebDriver):
        self.base_url = "https://www.baidu.com"
        super().__init__(self.base_url, driver)

        self.search_input_path = "//input[@name='wd']"

        self.setting_span_path = "//span[contains(text(),'设置')]"
        self.search_setting_a_path = "//span[contains(text(),'搜索设置')]"
        self.save_setting_a_path = "//a[contains(text(),'保存设置')]"

    def search(self, search_term: str):
        search_box = self._wait_find(self.search_input_path)
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        self._wait(self.driver).until(title_contains(search_term))

    def settings(self):
        settings_link = self._wait_find(self.setting_span_path)
        settings_link.click()

        search_setting = self._wait_find(self.search_setting_a_path)
        search_setting.click()

        save_setting = self._wait_find(self.save_setting_a_path)
        save_setting.click()

        self._wait(self.driver).until(alert_is_present())
