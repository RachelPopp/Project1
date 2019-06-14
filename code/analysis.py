import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Function to clean up any data, do whatever to df_songs.
def clean_columns(df_songs, DEBUG):

    print("Beginning analysis...")

    # Determining type of each received data by looking at row 0, and column content (after transpose, so terminal displays easier)
    if DEBUG:
        df_songs_type = df_songs.head(1).T
        # hackish way to find type of each element. There's probably a better way but don't know atm
        # for x in df_songs.iloc[0] : print(f"-- data: {x}\n-- is type: {type(x)}\n")
        print(f"-- first row of data is:\n{df_songs_type}")

    return (df_songs)

def graph(df_songs):
    pass