import pandas as pd
import numpy as np

# Method Chain 1 (Load data and deal with missing data)


def unprocessed(csv_file):
    #Takes in a csv file and returns a panads dataframe.
    df = pd.read_csv(csv_file, sep=";")
    return df

# Method Chain 2 (Create new columns, drop others, and do processing)

def load_and_process(csv_file):
    # Takes in a csv file and returns a cleaned dataframe by dropping unnecassry columns and null values and rows. In addition it merges duplicate values where appropriate.
    df = pd.read_csv(csv_file, sep=";")
    df1=(
        df.drop(["Date_of_birth", "TEAM", "Place_of_birth", "Saves", "Save_Percentage", "Shutouts", "Goals_Against", "Goals_Against_Average", "Shots_Against",
                    "Time_on_Ice_per_Game", 'Games_Started', 'Number', "Overtime_Losses", "Ties", "PowerPlay_Goals", "PowerPlay_Assists", "Short_Goals",
                    "Short_Assists", "Game_Tying_Goals", "SEASON", "Game_Winning_Goals", "Production", "Wins", "Losses", "Experience", "PlusMinus_Ratings", "Penalty_Minutes",
                    "Position"], axis=1))
    df2 = (
        df1.drop(df[df["SEASON_year"] < 2000].index)
           .reset_index(drop=True))
    
    df3 = (
        df2.dropna()
           .reset_index(drop=True))
    df4 = (
        df3.groupby(["Name","Height","Weight","Body_mass_index"],as_index=False)[["Games_Played","Goals", "Assists", "Shots_on_Goal", "Points"]].sum())
   
    return df4

    # Creates Dataframe with top Scorers

def topScorers(csv_file):
    df = pd.read_csv(csv_file, sep=";")
    df1=(
        df.drop(["Date_of_birth", "TEAM", "Place_of_birth", "Saves", "Save_Percentage", "Shutouts", "Goals_Against", "Goals_Against_Average", "Shots_Against",
                    "Time_on_Ice_per_Game", 'Games_Started', 'Number', "Overtime_Losses", "Ties", "PowerPlay_Goals", "PowerPlay_Assists", "Short_Goals",
                    "Short_Assists", "Game_Tying_Goals", "SEASON", "Game_Winning_Goals", "Production", "Wins", "Losses", "Experience", "PlusMinus_Ratings", "Penalty_Minutes",
                    "Position"], axis=1))
    df2 = (
        df1.drop(df[df["SEASON_year"] < 2000].index)
           .reset_index(drop=True))
    
    df3 = (
        df2.dropna()
           .reset_index(drop=True))
    df4 = (
        df3.groupby(["Name","Height","Weight","Body_mass_index"],as_index=False)[["Games_Played","Goals", "Assists", "Shots_on_Goal", "Points"]].sum())
   
    df4["Succesful Players"]=df4["Goals"]>300
   
    df5 = (
        df4.drop(df4[df4["Succesful Players"] == False].index)
           .reset_index(drop=True))
   
    return df5

    

    # Make sure to return the latest dataframe
