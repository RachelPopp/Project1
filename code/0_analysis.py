# Import Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, csv, sys
# import csv
# import sys

# grabbing the hdf5_getters.py file stored alongside analysis.py. We use it to save us major time converting from the h5 files
# into a data format that we can use; is also already formatted specifically for the million-song dataset
import hdf5_getters as hg

# Debug section; either True or False (1 or 0)
DEBUG = True
test_length = 5

# -----------------------------------

# the above steps take a little while, so
if DEBUG : print("-- Done importing")

# Organizing functions and names in one location; helps organization and automates dataframe column index later
# IF YOU WANT TO ADD MORE THINGS TO TRACK AND ANALYZE, ADD TO HERE FOLLOWING THE EXISTING STRUCTURE (see hdf5_getters.py for options)
hg_methods_dict = {
    "Number of Songs":hg.get_num_songs,
    "Artist Familiarity":hg.get_artist_familiarity,
    "Duration":hg.get_duration,
    "Title":hg.get_title}

# Initializing datatypes & counters we'll need later
file_no = 0
# dynamically generate df_songs index from keys in hg_methods_dict. Note that we transpose after setting the index, to get column titles
df_songs = pd.DataFrame(index = [x for x in hg_methods_dict]).T

if DEBUG : print(f"-- Target directory: {os.path.join(os.getcwd(),'..','MillionSongSubset','data')}\n-- type(os.getcwd()): {type(os.getcwd())}")

# Main loop to walk through all songs; uses users project install directory, but must be changed if we edit where the millionsong dataset is located
for subdir, dirs, files in os.walk(os.path.join(os.getcwd(),'..','MillionSongSubset','data')):
    for file in files:

        # if DEBUG : print(f"-- file: {file}")
        
        # open currently selected file (e.g. .../Z/I/TRAAAAW128F429D538.h5)
        hfile = hg.open_h5_file_read(os.path.join(subdir, file))

        data = []

        # loop thru the list of methods we want data of, established earlier.
        # Our 10k song data contains no files with multiple songs, but full might not(!)
        for method in hg_methods_dict.values():
            # for each method (grabbing duration, title, etc) append it to a temporary list
            data.append(method(hfile))

        # once all methods finished, append row to dataframe 
        df_songs = df_songs.append(pd.Series(data, index=df_songs.columns), ignore_index=True)

        hfile.close()

        # keep track of what file we're on, and exit early if DEBUG = True
        file_no += 1
        if DEBUG & (file_no > test_length):
            break
    if DEBUG & (file_no > test_length):
        break

if DEBUG : print(f"-- sys.getsizeof(df_songs) [size in bytes]: {sys.getsizeof(df_songs)}")
# Printing dataframe to csv, unless larger than 100mb; if we get a hellabig frame, we'll want to split this up. 
if sys.getsizeof(df_songs) < (100000000):
    with open(os.path.join(os.getcwd(),'..','code_output','big_songs_df.csv'), 'w') as output_file:
        writer = csv.writer(output_file)
        df_songs.to_csv(output_file)