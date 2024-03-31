from selenium import webdriver

from bilibili import Bilibili

driver = webdriver.Chrome()

try:
    bilibili = Bilibili(driver)
    bilibili.driver.get(bilibili.url)
    bilibili.process_cards()
except Exception as e:
    print(e)
finally:
    driver.quit()
