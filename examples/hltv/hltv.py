from webwalker import WebWalker
from locators import HLTVLocators


class HLTVWalker(WebWalker):

    def actual_date(self):
        date: str = self.text_of_this_element(HLTVLocators.RATING)
        return date.split('on')[1].strip()
