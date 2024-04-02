from selenium import webdriver

from baidu import Baidu

driver = webdriver.Chrome()

try:
    baidu = Baidu(driver)
    baidu.driver.get(baidu.url)
    baidu.search()
    baidu.settings()
except Exception as e:
    raise e
finally:
    driver.quit()

