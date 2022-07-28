from selenium.webdriver.common.by import By


class HLTVLocators:
    URL = 'https://www.hltv.org/ranking/teams/'
    RATING = (By.CSS_SELECTOR, ".regional-ranking-header")
