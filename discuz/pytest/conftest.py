import pytest
from selenium import webdriver

from discuz import process
from discuz.page.main_page import MainPage
from discuz.page.board_page import BoardPage
from discuz.process import load_test_data


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


@pytest.fixture(scope="session", autouse=True)
def clear_posts_before_and_after_tests(main_page, board_page):
    # Load posts to get board names
    test_data = load_test_data()
    board_names = set(post["board_name"] for post in test_data["posts"])

    # Clear posts from all boards before tests
    main_page.sign_in("admin", "admin")
    assert main_page.is_signed_in()

    for board_name in board_names:
        process.clear_posts(main_page, board_page, board_name)

    main_page.sign_out()

    yield

    # Clear posts from all boards after tests
    main_page.sign_in("admin", "admin")
    assert main_page.is_signed_in()

    for board_name in board_names:
        process.clear_posts(main_page, board_page, board_name)

    main_page.sign_out()
