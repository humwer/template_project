from selenium.webdriver.common.by import By


class TestSite:
    TEST_URL = "http://automationpractice.com/index.php"
    TEST_BUTTON_GO_TO_CATALOG = (By.CSS_SELECTOR, "a[title=Women]")
    TEST_IS_WOMEN_PAGE = (By.CSS_SELECTOR, ".navigation_page")
    TEST_CATEGORY_TOPS = (By.CSS_SELECTOR, "#layered_category_4")
    TEST_CATEGORY_DRESSES = (By.CSS_SELECTOR, "#layered_category_8")
    TEST_HAS_CATEGORY = (By.CSS_SELECTOR, ".cat-name")


