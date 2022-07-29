from selenium.webdriver.common.by import By


class VLRGGLocators:
    URL = 'https://www.vlr.gg/rankings'
    REGION = (By.CSS_SELECTOR, "h2.wf-label")
    TABLE_REGION = (By.CSS_SELECTOR, "table.mod-teams")
    TEAM = (By.CSS_SELECTOR, "tr.wf-card")
    TEAM_PLACE = (By.CSS_SELECTOR, "td.rank-item-rank a")
    TEAM_NAME_AND_COUNTRY = (By.CSS_SELECTOR, "td.rank-item-team a > div")
    TEAM_SCORE = (By.CSS_SELECTOR, "td.rank-item-rating")
