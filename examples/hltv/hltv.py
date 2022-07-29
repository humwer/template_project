from webwalker import WebWalker
from locators import HLTVLocators


class HLTVWalker(WebWalker):

    def actual_date(self):
        date: str = self.text_of_element(HLTVLocators.RATING)
        if date is None:
            return False
        else:
            return date.split('on')[1].strip()

    def skip_cookies(self):
        self.click_element(HLTVLocators.COOKIES_BUTTON)

    def get_team_names(self):
        teams: list = self.text_of_elements(HLTVLocators.TEAM_NAME)
        if teams is None:
            return False
        else:
            return teams

    def get_points_teams(self):
        points: list = self.text_of_elements(HLTVLocators.TEAM_POINTS)
        if points is None:
            return False
        else:
            return points

    def get_team_players(self):
        self.click_element(HLTVLocators.TEAM_PLAYERS)
        elements: list = self.get_elements(HLTVLocators.TEAM_PLAYERS)
        if elements is None:
            return False
        team_players: list = []
        for players in elements:
            team_players.append(self.text_of_elements(HLTVLocators.PLAYER, players))
        if team_players is None:
            return False
        else:
            return team_players
