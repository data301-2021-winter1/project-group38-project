import pandas as pd

def unprocessed(path):
    df = pd.read_csv(path)
    return df

def load_and_process(path):
    df1 = (
        pd.read_csv(path, sep = ';')
        .drop(["Date_of_birth","SEASON", "TEAM", "Points", "PlusMinus_Ratings", "Penalty_Minutes", "PowerPlay_Goals", "PowerPlay_Assists", "Short_Goals", "Short_Assists",
               "Game_Winning_Goals", "Game_Tying_Goals", "Production", "Number", "Games_Started", "Wins", "Losses",
               "Ties", "Overtime_Losses", "Goals_Against", "Goals_Against_Average", "Shots_Against", "Saves", "Save_Percentage", "Shutouts",
               "Place_of_birth", "Shooting_Percentage", "Time_on_Ice_per_Game", "Age", "Experience"], axis = 1)
        .dropna()
    )
    return df1
