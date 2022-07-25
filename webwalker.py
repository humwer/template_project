from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


class WebWalker:

    def __init__(self, url: str):
        self.url = url
        self.options = Options()
        self.options.add_argument(f'user-agent={UserAgent().random}')
        self.browser = webdriver.Chrome(options=self.options)
        self.wait_time = 10
        print("[+] Opened browser Google Chrome")

    def __del__(self):
        pass

    def go_to_url(self, url: str = None):
        pass

    def click_this_button(self, selectors: tuple):
        pass

    def text_of_the_element(self, selectors: tuple):
        pass

    def fill_this_element(self, selectors: tuple, fill_text: str = None):
        pass
