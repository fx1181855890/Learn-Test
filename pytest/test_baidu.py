from baidu import Baidu


def test_baidu_search():
    baidu = Baidu()
    baidu.search()
    assert "pytest" in baidu.driver.title


def test_baidu_settings():
    baidu = Baidu()
    baidu.settings()
    alert = baidu.driver.switch_to.alert
    assert alert
