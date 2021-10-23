import pandas as pd
def load_and_process(path):

    # Method Chain 1 (Load data and deal with missing data)
    df1 = (
        pd.read_csv(path, sep = ';')
        .drop(["Date_of_birth","SEASON", "TEAM", "Points", "PlusMinus_Ratings", "Penalty_Minutes", "PowerPlay_Goals", "PowerPlay_Assists",
                                       "Short_Goals", "Short_Assists", "Game_Winning_Goals", "Game_Tying_Goals", "Production", "Number", "Games_Started", "Wins", "Losses",
                                      "Ties", "Overtime_Losses", "Goals_Against", "Goals_Against_Average", "Shots_Against", "Saves", "Save_Percentage", "Shutouts",
                                       "Place_of_birth", "Shooting_Percentage", "Time_on_Ice_per_Game", "Age", "Experience"], axis = 1)
        .dropna()  
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)


    df2 = (
        df1[df1.SEASON_year >= 2000]
        .drop("SEASON_year", axis = 1)
        .groupby(['Name', 'Position', 'Height', 'Weight', 'Body_mass_index'], as_index = False)[["Games_Played","Goals", "Assists", "Shots_on_Goal"]].sum()
    )

    # Make sure to return the latest dataframe

    return df2