from selenium.webdriver.common.by import By


class HLTVLocators:
    URL = 'https://www.hltv.org/ranking/teams/'
    COOKIES_BUTTON = (By.CSS_SELECTOR, "#CybotCookiebotDialogBodyButtonDecline")
    RATING = (By.CSS_SELECTOR, ".regional-ranking-header")
    TEAM_POSITION = (By.CSS_SELECTOR, ".ranking-header .position")
    TEAM_NAME = (By.CSS_SELECTOR, ".teamLine > .name")
    TEAM_POINTS = (By.CSS_SELECTOR, ".teamLine > .points")
    TEAM_PLAYERS = (By.CSS_SELECTOR, ".playersLine")
    PLAYER = (By.CSS_SELECTOR, ".rankingNicknames > span")
