from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import *

from scraper import Scraper


class Baidu(Scraper):
    def __init__(self):
        super().__init__("https://www.baidu.com")

        self.search_input_path = "//input[@name='wd']"

        self.setting_a_path = "//a[contains(text(),'设置')]"
        self.search_setting_a_path = "//span[contains(text(),'搜索设置')]"
        self.save_setting_a_path = "//a[contains(text(),'保存设置')]"

    def search(self):
        search_box = self._wait_find(self.search_input_path)
        search_box.send_keys("pytest")
        search_box.send_keys(Keys.RETURN)

        self._wait(self.driver).until(title_contains("pytest"))
        assert True

    def settings(self):
        settings_link = self._wait_find(self.setting_a_path)
        settings_link.click()

        search_setting = self._wait_find(self.search_setting_a_path)
        search_setting.click()

        save_setting = self._wait_find(self.save_setting_a_path)
        save_setting.click()

        self._wait(self.driver).until(alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

        assert True
