from webwalker import WebWalker
from locators import HLTVLocators


class HLTVWalker(WebWalker):

    def actual_date(self):
        date: str = self.text_of_this_element(HLTVLocators.RATING)
        if date is None:
            return False
        else:
            return date.split('on')[1].strip()

    def skip_cookies(self):
        self.click_this_element(HLTVLocators.COOKIES_BUTTON)

