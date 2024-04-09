import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from baidu import Baidu


@pytest.mark.parametrize(
    "search_term, expected_title",
    [
        ("pytest", "pytest"),
        ("selenium", "selenium"),
        ("Python", "Python"),
    ],
)
def test_baidu_search(driver: WebDriver, search_term: str, expected_title: str) -> None:
    baidu = Baidu(driver)
    baidu.search(search_term)
    assert expected_title in baidu.driver.title


def test_baidu_settings(driver: WebDriver):
    baidu = Baidu(driver)
    baidu.settings()
    alert = baidu.driver.switch_to.alert
    assert alert
