from baidu import Baidu

try:
    baidu = Baidu()
    baidu.search()
    baidu.settings()
except Exception as e:
    raise e

