# Import Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys, os

# grabbing the hdf5_getters.py file stored alongside analysis.py. We use it to save us major time converting from the h5 files
# into a data format that we can use; is also already formatted specifically for the million-song dataset
import hdf5_getters as hg

# code to save our dataframe to csv
from save_df import save

import analysis

# the above steps take a little while, so whether debug or not, print
print("Done importing")
print("Rachel's Check")

# Debug section; either True or False (1 or 0)
DEBUG = False
test_length = 10
if DEBUG : print(f'-- DEBUG MODE ON')

# -----------------------------------

# Organizing functions and names in one location; helps organization and automates dataframe column index later
# IF YOU WANT TO ADD MORE THINGS TO TRACK AND ANALYZE, ADD TO HERE FOLLOWING THE EXISTING STRUCTURE (see hdf5_getters.py for options)
hg_methods_dict = {
    "Number of Songs":hg.get_num_songs,
    "Artist Name":hg.get_artist_name,
    "Artist Location":hg.get_artist_location,
    "Duration":hg.get_duration,
    "Title":hg.get_title,
    "Release":hg.get_release,
    "Year":hg.get_year,
    "Danceability":hg.get_danceability,
    "Energy":hg.get_energy,
    "Mode":hg.get_mode,
    "Tempo":hg.get_tempo
    }

# Initializing datatypes & counters we'll need later
file_no = 0
# dynamically generate df_songs column from keys in hg_methods_dict
df_songs = pd.DataFrame(columns = [x for x in hg_methods_dict])
print(df_songs)

if DEBUG : print(f"-- target directory: {os.path.join('..','MillionSongSubset','data')}")

# Main loop to walk through all songs; must be changed if we edit where the millionsong dataset is located
for subdir, dirs, files in os.walk(os.path.join('..','MillionSongSubset','data')):
    for file in files:

        # Note, this "progress bar" will only work if there's no other print statements in the loop! Comment both lines out if you want to debug in the middle of the loop
        sys.stdout.write(f"\rWorking on file no: {file_no}")
        sys.stdout.flush()

        # if DEBUG : print(f"-- file: {file}")
        
        # open currently selected file (e.g. .../Z/I/TRAAAAW128F429D538.h5)
        hfile = hg.open_h5_file_read(os.path.join(subdir, file))

        data = []

        # loop thru the list of methods we want data of, established earlier.
        # Our 10k song data contains no files with multiple songs, but full might not(!)
        # for each method (grabbing duration, title, etc) append it to a temporary list
        for hg_method in hg_methods_dict.values():

            # get datum for this particular method
            datum = hg_method(hfile)

            # checking if datum is in the default "b'stringything'" format of np.bytes_, and converting back to str. Will likely be other data filtering needed later
            if isinstance(datum, np.bytes_):
                # I'm getting unicode errors on this one, see unicode_save_issue.py
                # if file_no == 471 : print(datum)
                datum = datum.decode('UTF-8')

            # append datum to working list, which will soon become a row in df_songs
            data.append(datum)

        # once all methods finished, append row to dataframe 
        df_songs = df_songs.append(pd.Series(data, index=df_songs.columns), ignore_index=True)

        # close current file
        hfile.close()

        # keep track of what file we're on, and exit loop if DEBUG == True and at our limit
        file_no += 1
        if DEBUG & (file_no > test_length):
            break
    if DEBUG & (file_no > test_length):
        break
# new line after the progressbar
print()

# Just checking how big the filesize gets
if DEBUG : print(f"-- sys.getsizeof(df_songs) [size in bytes]: {sys.getsizeof(df_songs)}")

# Printing dataframe to csv via the save_df.py method, unless larger than 100mb; if we get a hellabig frame, we ought to split it up. 
if sys.getsizeof(df_songs) < (100000000): save(df_songs)

# One option to handle passing dataframes to different location
analysis.clean_columns(df_songs, DEBUG)