import pytest

from baidu import Baidu


@pytest.mark.parametrize(
    "search_term, expected_title",
    [
        ("pytest", "pytest"),
        ("selenium", "selenium"),
        ("Python", "Python"),
    ],
)
def test_baidu_search(search_term: str, expected_title: str) -> None:
    baidu = Baidu()
    baidu.search(search_term)
    assert expected_title in baidu.driver.title


def test_baidu_settings():
    baidu = Baidu()
    baidu.settings()
    alert = baidu.driver.switch_to.alert
    assert alert
