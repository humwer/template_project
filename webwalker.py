from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from random import randrange
import time
import re

DELAY = True


def real_user(do_delay: bool = True):
    """Decorator used for imitation delay of acts of user"""
    def _real_user(method):
        def sleeping(*args, **kwargs):
            if do_delay:
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

    def __init__(self, url: str, option_launch_browser: bool = False, option_debug: bool = False):
        """Support class used for creation new classes of parsers\n
        Parameters:
            url: link to website, e.g. https:\\example.com
            option_launch_browser: option of launch browser.
                If you want launch - True. Unless you want - False.
            option_debug: Option of debugging (only for success-messages).
                If you want print messages - True. Unless you want - False.
        """
        self.url = url
        self.options = Options()
        self.options.add_argument(f'user-agent={UserAgent().random}')
        if option_launch_browser:
            self.options.add_argument('headless')
        self.browser = webdriver.Chrome(options=self.options)
        self.last_error = None
        self.wait_time = 10
        self.debug = option_debug
        if self.debug:
            print("[+] Opened browser Google Chrome")

    def get_current_url(self):
        """Returns url of active tab or None if raise error"""
        try:
            url = self.browser.current_url
            if self.debug:
                print(f'[+] Now url: {url}')
            return url
        except WebDriverException:
            print('[-] My bad, I cant get url ><')
            return None

    def go_to_url(self, url: str = None):
        """Surf to specified link or link in class-object\n
        Parameters:
            url: link to website, e.g. https:\\example.com
        """
        if url is None:
            url = self.url
        try:
            self.browser.get(url)
            if self.debug:
                print(f'[+] Surfed to: {url}')
            self.last_error = None
        except ValueError:
            print('[-] I cant go here ><')
            self.last_error = ValueError

    @real_user(do_delay=DELAY)
    def click_this_element(self, selectors: tuple):
        """Click by specified element of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
        """
        try:
            if self.last_error is None:
                button = WebDriverWait(self.browser, self.wait_time).\
                    until(EC.presence_of_element_located(selectors))
                if self.debug:
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

    @real_user(do_delay=DELAY)
    def text_of_this_element(self, selectors: tuple):
        """Get text from element of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
        Returns:
            text
             OR None (if error)
        """
        try:
            if self.last_error is None:
                WebDriverWait(self.browser, self.wait_time). \
                    until(EC.presence_of_element_located(selectors))
                element = self.browser.find_element(*selectors)
                if self.debug:
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

    @real_user(do_delay=DELAY)
    def text_of_this_elements(self, selectors: tuple):
        """Get text from elements of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
        Returns:
             list with texts
             OR None (if error)
        """
        try:
            if self.last_error is None:
                WebDriverWait(self.browser, self.wait_time). \
                    until(EC.presence_of_element_located(selectors))
                elements = self.browser.find_elements(*selectors)
                text_elements = [element.text for element in elements]
                if self.debug:
                    print(f"[+] Text of this elements: {text_elements}")
                return text_elements
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

    @real_user(do_delay=DELAY)
    def get_attribute_of_element(self, selectors: tuple, name_attribute: str):
        """Get attribute from element of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            name_attribute: name of attribute, e.g. 'class', 'data-qa', 'href'
        Returns:
            value of attribute
             OR None (if error)
        """
        try:
            WebDriverWait(self.browser, self.wait_time). \
                until(EC.presence_of_element_located(selectors))
            if self.last_error is None:
                element = self.browser.find_element(*selectors)
                if self.debug:
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

    @real_user(do_delay=DELAY)
    def get_attribute_of_elements(self, selectors: tuple, name_attribute: str):
        """Get attributes from elements of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            name_attribute: name of attribute, e.g. 'class', 'data-qa', 'href'
        Returns:
            list with values of attributes
             OR None (if error)
        """
        try:
            if self.last_error is None:
                WebDriverWait(self.browser, self.wait_time). \
                    until(EC.presence_of_element_located(selectors))
                elements = self.browser.find_elements(*selectors)
                attr_elements = [element.get_attribute(name_attribute) for element in elements]
                if self.debug:
                    print(f"[+] Attribute of this elements: '{attr_elements}'")
                return attr_elements
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

    @real_user(do_delay=DELAY)
    def get_element(self, selectors: tuple):
        """Get element of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
        Returns:
            element
             OR None (if error)
        """
        try:
            if self.last_error is None:
                WebDriverWait(self.browser, self.wait_time). \
                    until(EC.presence_of_element_located(selectors))
                element = self.browser.find_element(*selectors)
                if self.debug:
                    print(f"[+] Element by '{selectors}'")
                return element
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

    @real_user(do_delay=DELAY)
    def get_elements(self, selectors: tuple):
        """Get elements of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
        Returns:
            list with elements
             OR None (if error)
        """
        try:
            if self.last_error is None:
                WebDriverWait(self.browser, self.wait_time). \
                    until(EC.presence_of_element_located(selectors))
                elements = self.browser.find_elements(*selectors)
                if self.debug:
                    print(f"[+] Elements: '{selectors}'")
                return elements
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

    @real_user(do_delay=DELAY)
    def fill_this_element(self, selectors: tuple, fill_text: str = None):
        """Fill specified element of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            fill_text: data for filling
        """
        try:
            if self.last_error is None:
                element = WebDriverWait(self.browser, self.wait_time).\
                    until(EC.presence_of_element_located(selectors))
                element.send_keys(fill_text)
                if self.debug:
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

    def find_text_in_this_element_by_regex(self, selectors: tuple, regex: str):
        """Get text by regex from elements of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            regex: regular expression should be raw-string, e.g. r'[0-9]{1,3}', r'[A-Za-z]' and etc.
        Returns:
            text
             OR None (if error)
        """
        try:
            if self.last_error is None:
                element = WebDriverWait(self.browser, self.wait_time).\
                    until(EC.presence_of_element_located(selectors))
                found_matches = re.findall(regex, element.text)
                if len(found_matches) == 0:
                    print(f"[-] Not found matches in this element by regex: '{regex}'")
                    return found_matches
                else:
                    if self.debug:
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
