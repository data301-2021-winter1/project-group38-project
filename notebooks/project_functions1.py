import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file,sep=";")
          


          # etc...
      )
    # Method Chain 2 (Create new columns, drop others, and do processing)
    df2 = (df1
        .dropna()
          )
    return df2

    # Make sure to return the latest dataframe
