import pandas as pd
import numpy as np

# Method Chain 1 - Loading the datafile

def unprocessed(csv_file):
    df = pd.read_csv(csv_file, sep=";")
    return df

# Method Chain 2 - Process the data

def intial_process(csv_file):
    df = pd.read_csv(csv_file, sep=";")
    df1 = (
        df.drop(df.columns[[1,3,4,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,36,37]], axis=1))
    df2 = (
        df1.drop(df[df["SEASON_year"] < 1988].index)
           .reset_index(drop=True))
        
    return df2
        
# Method Chain 3 - To create a list of MVP seasons from 2001-2018

def mvp_seasons(csv_file):
    df = pd.read_csv(csv_file, sep=";")
    mvp_dict = {
    'Name': ['Taylor Hall', 'Connor McDavid', 'Patrick Kane', 'Sidney Crosby', 'Alex Ovechkin', 'Evgeni Malkin', 'Corey Perry', 'Henrik Sedin', 'Alex Ovechkin', 'Alex Ovechkin', 'Sidney Crosby', 'Joe Thornton', 'Martin St. Louis', 'Peter Forsberg', 'Joe Sakic'],
    'SEASON_year': [2018, 2017, 2016, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2004, 2003, 2001],
    'MVP': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes']
}
    mvp_df = pd.DataFrame(mvp_dict)
    df1 = (
        df.drop(df.columns[[1,3,4,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,36,37]], axis=1))
    df2 = (
        df1.drop(df[df["SEASON_year"] < 1988].index)
           .reset_index(drop=True))
    df3 = (
        pd.merge(df2, mvp_df))
    df4 = (
        df3.mergeby(["Name", "SEASON_year", "Position", "Height", "Weight", "Age", "Experience", "MVP"],as_index=False)[["Games_Played","Goals", "Assists","Points", "PlusMinus_Ratings", "Game_Winning_Goals"]].sum())
        
    return df4