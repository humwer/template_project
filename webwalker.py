from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from random import randrange
import time


def real_user(method):
    def sleeping(*args, **kwargs):
        rand_int = randrange(3, 5)
        if rand_int == 1:
            print(f'[?] Please, wait for {rand_int} second')
        else:
            print(f'[?] Please, wait for {rand_int} seconds')
        time.sleep(rand_int)
        method(*args, **kwargs)
    return sleeping


class WebWalker:

    def __init__(self, url: str):
        self.url = url
        self.options = Options()
        self.options.add_argument(f'user-agent={UserAgent().random}')
        self.browser = webdriver.Chrome(options=self.options)
        self.wait_time = 10
        print("[+] Opened browser Google Chrome")

    def __del__(self):
        self.browser.quit()

    def go_to_url(self, url: str = None):
        if url is None:
            url = self.url
        try:
            self.browser.get(url)
            print(f'[+] Went to: {url}')
        except ValueError:
            print('[-] I cant go here ><')

    @real_user
    def click_this_button(self, selectors: tuple):
        try:
            button = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located(selectors))
            print(f"[+] Clicked button: '{button.text}'")
            button.click()
        except TimeoutException:
            print(f"[-] My bad, I don't find '{selectors}' -> button ._.")

    @real_user
    def text_of_the_element(self, selectors: tuple):
        try:
            element = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located(selectors))
            print(f"[+] Text of the element: '{element.text}'")
            return element.text
        except TimeoutException:
            print(f"[-] My bad, I don't find '{selectors}' -> element ._.")

    @real_user
    def fill_this_element(self, selectors: tuple, fill_text: str = None):
        try:
            element = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located(selectors))
            element.send_keys(fill_text)
            print(f"[+] Text '{fill_text}' in the element")
        except TimeoutException:
            print(f"[-] My bad, I cant set text '{fill_text}'")