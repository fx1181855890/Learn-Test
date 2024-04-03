from baidu import Baidu

try:
    baidu = Baidu()
    baidu.search()
    baidu.reset_to_homepage()
    baidu.settings()
except Exception as e:
    raise e

