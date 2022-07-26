from selenium.webdriver.common.by import By


class TestSite:
    URL = "http://automationpractice.com/index.php"
    BUTTON_GO_TO_CATALOG = (By.CSS_SELECTOR, "a[title=Women]")
    IS_CATALOG = (By.CSS_SELECTOR, ".navigation_page")
    CATEGORY_TOPS = (By.CSS_SELECTOR, "#layered_category_4")
    CATEGORY_DRESSES = (By.CSS_SELECTOR, "#layered_category_8")
    SELECTED_CATEGORIES = (By.CSS_SELECTOR, ".cat-name")


