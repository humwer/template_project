from hltv import HLTVWalker
from locators import HLTVLocators


if __name__ == '__main__':
    walker = HLTVWalker(HLTVLocators.URL, True)
    walker.go_to_url()
    rating_actual_date = walker.actual_date()
