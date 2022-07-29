from vlrgg import VLRGGWalker
from locators import VLRGGLocators
import json

if __name__ == '__main__':
    while True:
        walker = VLRGGWalker(VLRGGLocators.URL, option_launching_browser=True,
                             option_ignoring_error=False, debugging=True)
        walker.go_to_url()
        regions = walker.get_regions()
        tables_of_regions = walker.get_tables_regions()
        data: dict = {}
        for table, region in zip(tables_of_regions, regions):
            data[region] = []
            teams_of_table = [team for team in walker.get_teams_in_table(table)]
            for team in teams_of_table:
                data_team: dict = {}
                if team is None:
                    continue
                place = walker.get_place_of_team(team)
                if place is None:
                    walker.reset_last_error()
                    continue
                name = walker.get_name_of_team(team)
                country = walker.get_country_of_team(team)
                score = walker.get_score_of_team(team)
                data_team[name] = {'Place': place, 'Country': country, 'Score': score}
                data[region].append(data_team)

        with open('data.json', 'w', encoding='utf8') as output:
            json.dump(data, output, indent=4, ensure_ascii=False)

        break
