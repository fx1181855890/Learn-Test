from scrape.bilibili import Bilibili

try:
    bilibili = Bilibili()
    bilibili.process_cards()
except Exception as e:
    raise e
