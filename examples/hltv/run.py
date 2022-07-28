from hltv import HLTVWalker
from locators import HLTVLocators


if __name__ == '__main__':
    walker = HLTVWalker(HLTVLocators.URL, True)
    walker.go_to_url()
    walker.skip_cookies()
    rating_actual_date = walker.actual_date()
    teams_name = walker.get_team_names()
    teams_points = walker.get_points_teams()
