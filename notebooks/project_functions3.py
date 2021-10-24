import pandas as pd

def unprocessed(path):
    df = pd.read_csv(path, sep = ';')
    return df

def load_and_process(path):
    df = pd.read_csv(path, sep = ';')

    df1 = (
        df.drop(["Date_of_birth","SEASON", "TEAM", "Points", "PlusMinus_Ratings", "Penalty_Minutes", "PowerPlay_Goals", "PowerPlay_Assists", "Short_Goals", "Short_Assists",
               "Game_Winning_Goals", "Game_Tying_Goals", "Production", "Number", "Games_Started", "Wins", "Losses",
               "Ties", "Overtime_Losses", "Goals_Against", "Goals_Against_Average", "Shots_Against", "Saves", "Save_Percentage", "Shutouts",
               "Place_of_birth", "Shooting_Percentage", "Time_on_Ice_per_Game", "Age", "Experience"], axis = 1)
        .dropna()
    )
    df2 = (
        df1[df1.SEASON_year >= 2000].drop("SEASON_year", axis = 1)
    )
    df3 = (
        df2[df2.Position != 'Forward']
    )
    df4 = (
        df3.groupby(['Name', 'Position', 'Height', 'Weight', 'Body_mass_index'], as_index = False)[["Games_Played","Goals", "Assists", "Shots_on_Goal"]].sum()
    )
    return df4