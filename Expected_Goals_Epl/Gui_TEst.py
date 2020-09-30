import tkinter as tk
from tkinter import *
import pandas as pd

data = pd.read_csv("stats.csv", encoding='latin-1')
prem_Team_Names=["Arsenal", "Aston Villa", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leeds Utd" , "Leicester City", "Liverpool", "Newcastle Utd", "Manchester City", "Manchester Utd", "Sheffield Utd", "Southampton", "Tottenham", "West Brom", "West Ham Utd", "Wolverhampton"]


root = tk.Tk()
root.geometry("500x200")

home_team_var = tk.StringVar()
away_team_var = tk.StringVar()
home_team = ""
away_team = ""

def submit():
    home = str(home_entry.get())
    away = str(away_entry.get())

    def look_up(team):
        index = 0
        for team_prem in prem_Team_Names:
            if team == team_prem:
                return index
            index += 1

    home_team = look_up(home)
    away_team = look_up(away)

    scored_home = data["Goals_Scored_Home"][home_team] / data["Matches_Played"][home_team]
    conceded_home = data["Goals_Conceded_Home"][home_team] / data["Matches_Played"][home_team]

    scored_away = data["Goals_Scored_Away"][away_team] / data["Matches_Played"][away_team]
    conceded_away = data["Goals_Conceded_Away"][away_team] / data["Matches_Played"][away_team]


    home_team_goals = 1*(scored_home + conceded_away)
    away_team_goals = 1*(conceded_home + scored_away)

    name_result = str(prem_Team_Names[home_team]), " vs ", str(prem_Team_Names[away_team])
    score_result = round(home_team_goals, 1), "-", round(away_team_goals, 1)

    result_label_score = tk.Label(root, text= score_result)
    result_label_score.grid(row=5, column=1)
    result_label_name = tk.Label(root, text= name_result)
    result_label_name.grid(row=4, column=1)



    home_team_var.set("")
    away_team_var.set("")

home_label = tk.Label(root, text="Home_Team")
home_entry = tk.Entry(root, textvariable=home_team_var)

away_label = tk.Label(root, text="Away_Team")
away_entry = tk.Entry(root, textvariable=away_team_var)

sub_btn = tk.Button(root, text='Submit', command=submit)

home_label.grid(row=0, column=0)
home_entry.grid(row=1, column=0)

label_vs = tk.Label(root, text="vs").grid(row=1, column=1)

away_label.grid(row=0, column=3)
away_entry.grid(row=1, column=3)

sub_btn.grid(row=3, column=1)\

root.mainloop()
