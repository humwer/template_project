from selenium.webdriver.remote.webelement import WebElement
from webwalker import WebWalker
from locators import VLRGGLocators


class VLRGGWalker(WebWalker):

    def get_regions(self):
        regions: list = self.text_of_elements(VLRGGLocators.REGION)
        if regions is None:
            return None
        return regions

    def get_tables_regions(self):
        tables: list = self.get_elements(VLRGGLocators.TABLE_REGION)
        if tables is None:
            return None
        return tables

    def get_teams_in_table(self, table: WebElement):
        teams: list = self.get_elements(VLRGGLocators.TEAM, table)
        if teams is None:
            return []
        return teams

    def get_place_of_team(self, team: WebElement):
        place: str = self.text_of_element(VLRGGLocators.TEAM_PLACE, team)
        if place is None:
            return None
        return int(place)

    def get_name_of_team(self, team: WebElement):
        name_and_country: str = self.text_of_element(VLRGGLocators.TEAM_NAME_AND_COUNTRY, team)
        if name_and_country is None:
            return None
        name = name_and_country.split('\n')[0]
        return name

    def get_country_of_team(self, team: WebElement):
        name_and_country: str = self.text_of_element(VLRGGLocators.TEAM_NAME_AND_COUNTRY, team)
        if name_and_country is None:
            return None
        country = name_and_country.split('\n')[1]
        return country

    def get_score_of_team(self, team: WebElement):
        score: str = self.text_of_element(VLRGGLocators.TEAM_SCORE, team)
        if score is None:
            return None
        return int(score)
