from vlrgg import VLRGGWalker
from locators import VLRGGLocators
import json

if __name__ == '__main__':
    while True:
        # Flag for new loop if data isn't get
        new_loop_flag = False
        walker = VLRGGWalker(VLRGGLocators.URL, option_launching_browser=False,
                             option_ignoring_error=False, debugging=True)
        walker.go_to_url()
        regions = walker.get_regions()
        if not regions:
            walker.reset_last_error()
            continue
        tables_of_regions = walker.get_tables_regions()
        if not tables_of_regions:
            walker.reset_last_error()
            continue
        data: dict = {}
        for table, region in zip(tables_of_regions, regions):
            data[region] = []
            teams_of_table = [team for team in walker.get_teams_in_table(table)]
            if len(teams_of_table) == 0:
                walker.reset_last_error()
                continue
            for team in teams_of_table:
                data_team: dict = {}
                place = walker.get_place_of_team(team)
                if place is None:
                    new_loop_flag = True
                    walker.reset_last_error()
                    break
                name = walker.get_name_of_team(team)
                country = walker.get_country_of_team(team)
                score = walker.get_score_of_team(team)
                data_team[name] = {'Place': place, 'Country': country, 'Score': score}
                data[region].append(data_team)
            # Don't know how to do better yet
            if new_loop_flag:
                break
        # Don't know how to do better yet
        if new_loop_flag:
            continue

        with open('data.json', 'w', encoding='utf8') as output:
            json.dump(data, output, indent=4, ensure_ascii=False)

        break
