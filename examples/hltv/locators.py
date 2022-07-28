from selenium.webdriver.common.by import By


class HLTVLocators:
    URL = 'https://www.hltv.org/ranking/teams/'
    COOKIES_BUTTON = (By.CSS_SELECTOR, "#CybotCookiebotDialogBodyButtonDecline")
    RATING = (By.CSS_SELECTOR, ".regional-ranking-header")
    TEAM_NAME = (By.CSS_SELECTOR, ".teamLine > .name")
    TEAM_POINTS = (By.CSS_SELECTOR, ".teamLine > .points")
