from selenium import webdriver

from scrape.bilibili import Bilibili

driver = webdriver.Chrome()

try:
    bilibili = Bilibili(driver)
    bilibili.driver.get(bilibili.url)
    bilibili.process_cards()
except Exception as e:
    raise e
finally:
    driver.quit()
