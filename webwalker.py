from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
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
            if not any(isinstance(param, WebElement) for param in args):
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

    def __init__(self, url: str, option_launching_browser: bool = False,
                 option_ignoring_error: bool = False, debugging: bool = False):
        """Support class used for creation new classes of parsers\n
        Parameters:
            url: link to website, e.g. https:\\example.com
            option_launching_browser: option of launching browser.
                If you want launch - True. Unless you want - False.
            option_ignoring_error: option of ignoring errors  (warning: can raises crash)
                If you want to ignore - True. Unless you want - False.
            debugging: option of debugging (only for success-messages).
                If you want print messages - True. Unless you want - False.
        """
        self.url = url
        self.options = Options()
        self.options.add_argument(f'user-agent={UserAgent().random}')
        if not option_launching_browser:
            self.options.add_argument('headless')
        self.browser = webdriver.Chrome(options=self.options)
        self.__last_error = None
        self.__option_ignoring_error = option_ignoring_error
        self.wait_time = 10
        self.debug = debugging
        if self.debug:
            print("[+] Opened browser Google Chrome")

    @property
    def last_error(self):
        """Get last error"""
        return self.__last_error

    def reset_last_error(self):
        """Reset last error"""
        self.__last_error = None

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
            self.__last_error = None
        except ValueError:
            print('[-] I cant go here ><')
            self.__last_error = ValueError

    @real_user(do_delay=DELAY)
    def get_element(self, selectors: tuple, target_element: WebElement = None):
        """Get element of web page or target element\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            target_element: WebElement for looking for in it
        Returns:
            element
             OR None (if error or target_element isn't WebElement)
        """

        def _get_element(webelement):
            element = webelement.find_element(*selectors)
            if self.debug:
                print(f"[+] Element by '{selectors}'")
            return element

        try:
            if self.__last_error is None or self.__option_ignoring_error:
                if target_element is None:
                    WebDriverWait(self.browser, self.wait_time). \
                        until(EC.presence_of_element_located(selectors))
                    elem = _get_element(self.browser)
                    return elem
                else:
                    if not isinstance(target_element, WebElement):
                        print(f"[-] Target element: {selectors} isn't WebElement!")
                        return None
                    elem = _get_element(target_element)
                    return elem
            else:
                print("[x] Hey, I dont will do that while you not use func 'go_to_url',\n"
                      f"Because we have error: {self.__last_error}")
                return None
        except TimeoutException:
            print(f"[-] My bad, I don't find '{selectors}' -> element ._.")
            self.__last_error = TimeoutException
            return None
        except WebDriverException:
            print("[-] Wow, error. Maybe we have low timeout?")
            self.__last_error = WebDriverException
            return None

    @real_user(do_delay=DELAY)
    def get_elements(self, selectors: tuple, target_element: WebElement = None):
        """Get elements of web page or target element\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            target_element: WebElement for looking for in it
        Returns:
            list with elements
             OR None (if error)
        """

        def _get_elements(webelement):
            elements = webelement.find_elements(*selectors)
            if self.debug:
                print(f"[+] Elements by '{selectors}'")
            return elements

        try:
            if self.__last_error is None or self.__option_ignoring_error:
                if target_element is None:
                    WebDriverWait(self.browser, self.wait_time). \
                        until(EC.presence_of_element_located(selectors))
                    elems = _get_elements(self.browser)
                    return elems
                else:
                    if not isinstance(target_element, WebElement):
                        print(f"[-] Target element: {selectors} isn't WebElement!")
                        return None
                    elems = _get_elements(target_element)
                    return elems
            else:
                print("[x] Hey, I dont will do that while you not use func 'go_to_url',\n"
                      f"Because we have error: {self.__last_error}")
                return None
        except TimeoutException:
            print(f"[-] My bad, I don't find '{selectors}' -> element ._.")
            self.__last_error = TimeoutException
            return None
        except WebDriverException:
            print("[-] Wow, error. Maybe we have low timeout?")
            self.__last_error = WebDriverException
            return None

    def click_element(self, selectors: tuple):
        """Click by specified element of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
        """

        button = self.get_element(selectors)
        if button is None:
            print(f"[-] Can't click this element: {selectors}'")
        else:
            if self.debug:
                print(f"[+] Clicked element: '{button.text}'")
            button.click()

    def text_of_element(self, selectors: tuple, target_element: WebElement = None):
        """Get text from element of web page or target element\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            target_element: WebElement for looking for in it
        Returns:
            text
             OR None (if error or target_element isn't WebElement)
        """

        def _text_of_element(istarget: bool):
            if not istarget:
                element = self.get_element(selectors)
            else:
                element = self.get_element(selectors, target_element)
            if element is None:
                return None
            if self.debug:
                print(f"[+] Text of element {selectors}: '{element.text}'")
            return element.text

        if target_element is None:
            text = _text_of_element(False)
        else:
            text = _text_of_element(True)
        if text is None:
            print(f"[-] Can't get text from this element: {selectors}'")
            return None
        return text

    def text_of_elements(self, selectors: tuple, target_element: WebElement = None):
        """Get text from elements of web page or target element\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            target_element: WebElement for looking for in it
        Returns:
             list with texts
             OR None (if error)
        """

        def _text_of_elements(istarget: bool):
            if not istarget:
                elements = self.get_elements(selectors)
            else:
                elements = self.get_elements(selectors, target_element)
            if elements is None:
                return None
            text_elements = [element.text for element in elements]
            if self.debug:
                print(f"[+] Text of elements {selectors}: {text_elements}")
            return text_elements

        if target_element is None:
            text = _text_of_elements(False)
        else:
            text = _text_of_elements(True)
        if text is None:
            print(f"[-] Can't get text from this elements: {selectors}'")
            return None
        return text

    def get_attribute_of_element(self, selectors: tuple, name_attribute: str, target_element: WebElement = None):
        """Get attribute from element of web page or target element\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            name_attribute: name of attribute, e.g. 'class', 'data-qa', 'href'
            target_element: WebElement for looking for in it
        Returns:
            value of attribute
             OR None (if error or target_element isn't WebElement)
        """

        def _get_attribute_of_element(istarget: bool):
            if not istarget:
                element = self.get_element(selectors)
            else:
                element = self.get_element(selectors, target_element)
            if element is None:
                return None
            if self.debug:
                print(f"[+] Attribute of element {selectors}: '{element.get_attribute(name_attribute)}'")
            return element.get_attribute(name_attribute)

        if target_element is None:
            attr = _get_attribute_of_element(False)
        else:
            attr = _get_attribute_of_element(True)
        if attr is None:
            print(f"[-] Can't get attribute from this element: {selectors}'")
            return None
        return attr

    def get_attribute_of_elements(self, selectors: tuple, name_attribute: str, target_element: WebElement = None):
        """Get attributes from elements of web page or target element\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            name_attribute: name of attribute, e.g. 'class', 'data-qa', 'href'
            target_element: WebElement for looking for in it
        Returns:
            list with values of attributes
             OR None (if error)
        """

        def _get_attribute_of_elements(istarget: bool):
            if not istarget:
                elements = self.get_elements(selectors)
            else:
                elements = self.get_elements(selectors, target_element)
            if elements is None:
                return None
            attr_elements = [element.get_attribute(name_attribute) for element in elements]
            if self.debug:
                print(f"[+] Attribute of elements {selectors}: '{attr_elements}'")
            return attr_elements

        if target_element is None:
            attrs = _get_attribute_of_elements(False)
        else:
            attrs = _get_attribute_of_elements(True)
        if attrs is None:
            print(f"[-] Can't get attributes from this elements: {selectors}'")
            return None
        return attrs

    def fill_element(self, selectors: tuple, fill_text: str = None, target_element: WebElement = None):
        """Fill specified element of web page or target element\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            fill_text: data for filling
            target_element: WebElement for looking for in it
        """

        def _fill_element(istarget):
            if not istarget:
                element = self.get_element(selectors)
            else:
                element = self.get_element(selectors, target_element)
            if element is not None:
                element.send_keys(fill_text)
                if self.debug:
                    print(f"[+] Text '{fill_text}' in element: {selectors}")
            else:
                print(f"[-] Element {selectors} isn't fill")

        if target_element is None:
            _fill_element(False)
        else:
            _fill_element(True)

    def find_text_in_element_by_regex(self, selectors: tuple, regex: str):
        """Get text by regex from elements of web page\n
        Parameters:
            selectors: tuple of search method and value, e.g. (By.CSS_SELECTOR, '.class')
            regex: regular expression should be raw-string, e.g. r'[0-9]{1,3}', r'[A-Za-z]' and etc.
        Returns:
            text
             OR None (if error)
        """

        element = self.get_element(selectors)
        found_matches = re.findall(regex, element.text)
        if len(found_matches) == 0:
            print(f"[-] Not found matches in this element by regex: '{regex}'")
            return found_matches
        else:
            if self.debug:
                print(f"[+] Found matches: {len(found_matches)} "
                      f"in this element by regex: '{regex}'")
            return found_matches
