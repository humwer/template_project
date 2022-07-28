from hltv import HLTVWalker
from locators import HLTVLocators
import json
import re


def convert_time(hltv_time: str):
    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
              'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    raw_data = hltv_time.split(' ')
    month = months[raw_data[0]]
    day = raw_data[1][:-3]
    year = raw_data[2]
    return f'{year}-{month}-{day}'


if __name__ == '__main__':
    while True:
        walker = HLTVWalker(HLTVLocators.URL, True)
        walker.go_to_url()
        walker.skip_cookies()

        hltv_actual_date = walker.actual_date()
        if not hltv_actual_date:
            continue
        rating_actual_date = convert_time(hltv_time=hltv_actual_date)
        teams_name = walker.get_team_names()
        if not teams_name:
            continue
        teams_points = walker.get_points_teams()
        if not teams_points:
            continue
        teams_players = walker.get_team_players()
        if not teams_players:
            continue

        data: dict = {rating_actual_date: {}}
        for name, points, players in zip(teams_name, teams_points, teams_players):
            data[rating_actual_date][name] = {'points': re.findall('[0-9]{1,4}', points)[0], 'players': players}
        with open('data.json', 'w') as output:
            json.dump(data, output, indent=4)

        break
