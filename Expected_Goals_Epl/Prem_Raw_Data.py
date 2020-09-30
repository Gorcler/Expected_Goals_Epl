import requests
import pandas as pd
import numpy as np
import csv
from bs4 import BeautifulSoup

urls = ["https://www.soccerstats.com/homeaway.asp?league=england", "https://www.soccerstats.com/homeaway.asp?league=england_2020", "https://www.soccerstats.com/homeaway.asp?league=england_2019", "https://www.soccerstats.com/homeaway.asp?league=england_2018", "https://www.soccerstats.com/homeaway.asp?league=england_2017", "https://www.soccerstats.com/homeaway.asp?league=england_2016","https://www.soccerstats.com/homeaway.asp?league=england_2015","https://www.soccerstats.com/homeaway.asp?league=england_2014","https://www.soccerstats.com/homeaway.asp?league=england_2013"]
prem_Team_Names= ["Arsenal", "Aston Villa", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leeds Utd" , "Leicester City", "Liverpool", "Newcastle Utd", "Manchester City", "Manchester Utd", "Sheffield Utd", "Southampton", "Tottenham", "West Brom", "West Ham Utd", "Wolverhampton"]

output_file = csv.writer(open("stats.csv", "w"))
output_file.writerow(["Team_Name", "Matches_Played", "Goals_Scored_Home","Goals_Scored_Away","Goals_Conceded_Home", "Goals_Conceded_Away"])

for team_names in prem_Team_Names[0:20]:

    matches_played = 0
    goals_scored_home = 0
    goals_conceded_home = 0
    goals_scored_away = 0
    goals_conceded_away = 0

    for url in urls:
        page_1 = requests.get(url)

        source = page_1.content
        soup = BeautifulSoup(source, "html.parser")

        table_1 = soup.find_all("div",{"id": "h2h-team1"})
        table_2 = soup.find_all("div",{"id": "h2h-team2"})

        league_table_Home = table_1[0]
        league_table_Away = table_2[0]

        teams_Home = league_table_Home.find_all("tr")
        teams_Away = league_table_Away.find_all("tr")

        #home
        for team in teams_Home[1:21]:

            stats = team.find_all("td")
            team_name = stats[1].text
            team_name = team_name.strip('\n')
            team_name = team_name.strip('\t')

            if team_name == team_names:

                matches_played += float(stats[2].text)
                goals_scored_home += float(stats[6].text)
                goals_conceded_home += float(stats[7].text)

        #Away
        for team in teams_Away[1:21]:

            stats = team.find_all("td")
            team_name = stats[1].text
            team_name = team_name.strip('\n')
            team_name = team_name.strip('\t')

            if team_name == team_names:

                matches_played += float(stats[2].text)
                goals_scored_away += float(stats[6].text)
                goals_conceded_away += float(stats[7].text)


    print(team_names, " ",matches_played, " ", goals_scored_home," ", goals_scored_away," ", goals_conceded_home, " " , goals_conceded_away)
    output_file.writerow([team_names, matches_played, goals_scored_home, goals_scored_away, goals_conceded_home, goals_conceded_away])





