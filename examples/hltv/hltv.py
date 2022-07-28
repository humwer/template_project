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

    def get_team_names(self):
        teams: list = self.text_of_this_element(HLTVLocators.TEAM_NAME, True)
        if teams is None:
            return False
        else:
            return teams

    def get_points_teams(self):
        points: list = self.text_of_this_element(HLTVLocators.TEAM_POINTS, True)
        if points is None:
            return False
        else:
            return points

    def get_team_players(self):
        self.click_this_element(HLTVLocators.TEAM_PLAYERS)
        elements: list = self.get_element(HLTVLocators.TEAM_PLAYERS, True)
        if elements is None:
            return False
        team_players: list = []
        for players in elements:
            team_players.append([player.text for player in players.find_elements(*HLTVLocators.PLAYER)])
        if team_players is None:
            return False
        else:
            return team_players
