from selenium import webdriver

from bilibili import Bilibili

driver = webdriver.Chrome()

try:
    driver.get("https://www.bilibili.com")
    bilibili = Bilibili(driver)
    bilibili.search()
    bilibili.process_cards()
except Exception as e:
    print(e)
finally:
    driver.quit()
