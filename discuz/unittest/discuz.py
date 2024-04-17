from selenium.webdriver.remote.webdriver import WebDriver

from scraper import Scraper


class User(Scraper):
    def __init__(self, driver: WebDriver):
        self.base_url = "http://localhost:8080/admin.php"
        super().__init__(self.base_url, driver)
