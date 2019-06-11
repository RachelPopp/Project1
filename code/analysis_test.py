# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import pandas as pd

csvpath = os.path.join('..', 'code_output', 'big_songs_df.csv')

# Import the Analyst_Coding_Test_(1).csv file as a DataFrame
df_music = pd.read_csv(csvpath, encoding="ISO-8859-1")

print(df_music.head())
print(len(df_music))
