import pytest
from selenium import webdriver
from discuz.page.main_page import MainPage
from discuz.page.board_page import BoardPage


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope="session")
def board_page(driver):
    return BoardPage(driver)
