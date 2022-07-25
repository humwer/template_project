from selenium.webdriver.common.by import By


class GitHubPage:
    GITHUB_TEST_URL = "https://github.com/"
    GITHUB_TEST_INPUT = (By.CSS_SELECTOR, "input[data-test-selector=nav-search-input]")
    GITHUB_TEST_CLICK = (By.CSS_SELECTOR, "div[aria-label=humwer]")


