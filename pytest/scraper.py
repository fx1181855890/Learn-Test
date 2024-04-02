from urllib.parse import urlparse, urlunparse

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Scraper:
    def __init__(self, webdriver: WebDriver):
        self.driver = webdriver

    def _wait(self, element: WebDriver | WebElement = None, timeout=2) -> WebDriverWait:
        if element is None:
            element = self.driver
        return WebDriverWait(element, timeout=timeout)

    def _wait_find(self, path: str, element: WebDriver | WebElement = None, find_all=False) -> WebElement | list[WebElement]:
        if element is None:
            element = self.driver
        if find_all is False:
            return self._wait(element).until(presence_of_element_located((By.XPATH, path)))
        if find_all is True:
            return self._wait(element).until(presence_of_all_elements_located((By.XPATH, path)))

    def _wait_for_staleness(self, element, timeout=2):
        WebDriverWait(self.driver, timeout).until(staleness_of(element))
