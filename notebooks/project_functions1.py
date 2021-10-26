import pandas as pd
import numpy as np

# Method Chain 1 (Load data and deal with missing data)


def unprocessed(csv_file):
    df = pd.read_csv(csv_file, sep=";")
    return df


def load_and_process(csv_file):
    dfx = pd.read_csv(csv_file, sep=";")
    df1=(
        dfx.drop(["Date_of_birth", "TEAM", "Place_of_birth", "Saves", "Save_Percentage", "Shutouts", "Goals_Against", "Goals_Against_Average", "Shots_Against",
                    "Time_on_Ice_per_Game", 'Games_Started', 'Number', "Overtime_Losses", "Ties", "PowerPlay_Goals", "PowerPlay_Assists", "Short_Goals",
                    "Short_Assists", "Game_Tying_Goals", "SEASON", "Game_Winning_Goals", "Production", "Wins", "Losses", "Experience", "PlusMinus_Ratings", "Penalty_Minutes",
                    "Position"], axis=1))
    df2=(
        df1.drop(df1[df1["SEASON_year"] < 2000].index))
    return df2

    # etc...

    # Method Chain 2 (Create new columns, drop others, and do processing)

    # Make sure to return the latest dataframe
