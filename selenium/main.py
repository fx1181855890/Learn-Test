from selenium import webdriver

from bilibili import Bilibili

driver = webdriver.Chrome()

try:
    driver.get("https://www.bilibili.com")
    bilibili = Bilibili(driver)
    bilibili.search()
    driver.switch_to.window(driver.window_handles[1])
    bilibili.process_card()
except Exception as e:
    print(e)
finally:
    driver.quit()


