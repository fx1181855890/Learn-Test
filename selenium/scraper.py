from urllib.parse import urlparse, urlunparse

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def get_base_url(full_url):
    parsed_url = urlparse(full_url)
    base_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))
    return base_url


class Scraper:
    def __init__(self, webdriver: WebDriver):
        self.driver = webdriver

    def _wait(self, element: WebDriver | WebElement = None) -> WebDriverWait:
        if element is None:
            element = self.driver
        return WebDriverWait(element, timeout=1)

    def _wait_find(self, path: str, element: WebDriver | WebElement = None, find_all=False) -> WebElement | list[WebElement]:
        if element is None:
            element = self.driver
        if find_all is False:
            return self._wait(element).until(presence_of_element_located((By.XPATH, path)))
        if find_all is True:
            return self._wait(element).until(presence_of_all_elements_located((By.XPATH, path)))