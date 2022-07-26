from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from random import randrange
import time
import re

TIMEOUT = True


def real_user(do_timeout: bool = True):
    def _real_user(method):
        def sleeping(*args, **kwargs):
            if do_timeout:
                rand_int = randrange(3, 5)
                if rand_int == 1:
                    print(f'[*] Please, wait for {rand_int} second...')
                else:
                    print(f'[*] Please, wait for {rand_int} seconds...')
                time.sleep(rand_int)
            result = method(*args, **kwargs)
            return result
        return sleeping
    return _real_user


class WebWalker:

    def __init__(self, url: str, without_launch_browser: bool = False):
        self.url = url
        self.options = Options()
        self.options.add_argument(f'user-agent={UserAgent().random}')
        if without_launch_browser:
            self.options.add_argument('headless')
        self.browser = webdriver.Chrome(options=self.options)
        self.last_error = None
        self.wait_time = 10
        print("[+] Opened browser Google Chrome")

    def __del__(self):
        self.browser.quit()

    def go_to_url(self, url: str = None):
        if url is None:
            url = self.url
        try:
            self.browser.get(url)
            print(f'[+] Surfed to: {url}')
            self.last_error = None
        except ValueError:
            print('[-] I cant go here ><')
            self.last_error = ValueError

    @real_user(do_timeout=TIMEOUT)
    def click_this_element(self, selectors: tuple):
        try:
            if self.last_error is None:
                button = WebDriverWait(self.browser, self.wait_time).\
                    until(EC.presence_of_element_located(selectors))
                print(f"[+] Clicked element: '{button.text}'")
                button.click()
            else:
                print("[x] Hey, I dont will do that while you not use func 'go_to_url',\n"
                      f"Because we have error: {self.last_error}")
        except TimeoutException:
            print(f"[-] My bad, I don't find '{selectors}' -> element ._.")
            self.last_error = TimeoutException
        except WebDriverException:
            print("[-] Wow, error. Maybe we have low timeout?")
            self.last_error = WebDriverException

    @real_user(do_timeout=TIMEOUT)
    def text_of_this_element(self, selectors: tuple):
        try:
            if self.last_error is None:
                element = WebDriverWait(self.browser, self.wait_time).\
                    until(EC.presence_of_element_located(selectors))
                print(f"[+] Text of this element: '{element.text}'")
                return element.text
            else:
                print("[x] Hey, I dont will do that while you not use func 'go_to_url',\n"
                      f"Because we have error: {self.last_error}")
                return None
        except TimeoutException:
            print(f"[-] My bad, I don't find '{selectors}' -> element ._.")
            self.last_error = TimeoutException
            return None
        except WebDriverException:
            print("[-] Wow, error. Maybe we have low timeout?")
            self.last_error = WebDriverException
            return None

    @real_user(do_timeout=TIMEOUT)
    def fill_this_element(self, selectors: tuple, fill_text: str = None):
        try:
            if self.last_error is None:
                element = WebDriverWait(self.browser, self.wait_time).\
                    until(EC.presence_of_element_located(selectors))
                element.send_keys(fill_text)
                print(f"[+] Text '{fill_text}' in this element")
            else:
                print("[x] Hey, I dont will do that while you not use func 'go_to_url',\n"
                      f"Because we have error: {self.last_error}")
        except TimeoutException:
            print(f"[-] My bad, I cant set text '{fill_text}'")
            self.last_error = TimeoutException
        except WebDriverException:
            print("[-] Wow, error. Maybe we have low timeout?")
            self.last_error = WebDriverException

    @real_user(do_timeout=TIMEOUT)
    def find_text_in_this_element_by_regex(self, selectors: tuple, regex: str):
        try:
            if self.last_error is None:
                element = WebDriverWait(self.browser, self.wait_time).\
                    until(EC.presence_of_element_located(selectors))
                found_matches = re.findall(regex, element.text)
                if len(found_matches) == 0:
                    print(f"[-] Not found matches in this element by regex: '{regex}'")
                    return found_matches
                else:
                    print(f"[+] Found matches: {len(found_matches)} "
                          f"in this element by regex: '{regex}'")
                    return found_matches
            else:
                print("[x] Hey, I dont will do that while you not use func 'go_to_url',\n"
                      f"Because we have error: {self.last_error}")
                return []
        except TimeoutException:
            print(f"[-] My bad, I cant found text by regex: '{regex}'")
            self.last_error = TimeoutException
            return []
        except WebDriverException:
            print("[-] Wow, error. Maybe we have low timeout?")
            self.last_error = WebDriverException
            return []

    @real_user(do_timeout=TIMEOUT)
    def get_attribute_of_element(self, selectors: tuple, name_attribute: str):
        try:
            if self.last_error is None:
                element = WebDriverWait(self.browser, self.wait_time).\
                    until(EC.presence_of_element_located(selectors))
                print(f"[+] Attribute of this element: '{element.get_attribute(name_attribute)}'")
                return element.get_attribute(name_attribute)
            else:
                print("[x] Hey, I dont will do that while you not use func 'go_to_url',\n"
                      f"Because we have error: {self.last_error}")
                return None
        except TimeoutException:
            print(f"[-] My bad, I don't find '{selectors}' -> element ._.")
            self.last_error = TimeoutException
            return None
        except WebDriverException:
            print("[-] Wow, error. Maybe we have low timeout?")
            self.last_error = WebDriverException
            return None

    def get_current_url(self):
        try:
            url = self.browser.current_url
            print(f'[+] Now url: {url}')
            return url
        except WebDriverException:
            print('[-] My bad, I cant get url ><')
            return None
