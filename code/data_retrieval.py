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

from analysis import *

# the above steps take a little while, so whether debug or not, print
print("Done importing")

# Debug section; either True or False (1 or 0)
DEBUG = True
test_length = 100
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
    "Tempo":hg.get_tempo,
    "Loudness":hg.get_loudness,
    "Hotness":hg.get_song_hotttnesss
    }

# Initializing datatypes & counters we'll need later
file_no = 0
# dynamically generate df_songs column from keys in hg_methods_dict
df_songs = pd.DataFrame(columns = [x for x in hg_methods_dict])

if DEBUG : print(f"-- target directory: {os.path.join('..','MillionSongSubset','data')}")

# Main loop to walk through all songs; must be changed if we edit where the millionsong dataset is located
for subdir, dirs, files in os.walk(os.path.join('..','MillionSongSubset','data')):
    for file in files:

        # Note, this "progress bar" will only work if there's no other print statements in the loop! Use sys.stdout.write instead of print to avoid newlines, if you want output in main loop
        sys.stdout.write(f"\x1b[2K\rWorking on file no: {file_no:6d}")
        
        # open currently selected file (e.g. .../Z/I/TRAAAAW128F429D538.h5)
        hfile = hg.open_h5_file_read(os.path.join(subdir, file))

        data = []
        unicode_valid = True

        # loop thru the list of methods we want data of, established earlier.
        # Our 10k song data contains no files with multiple songs, but full might not(!)
        # for each method (grabbing duration, title, etc) append it to a temporary list
        for hg_method in hg_methods_dict.values():

            # get datum for this particular method
            datum = hg_method(hfile)

            # checking if datum is tyoe np.bytes_, and converting back to str
            # certain systems cannot save or print the unencoded info; attempts to print to confirm saving is possibe.
            if isinstance(datum, np.bytes_):
                try:
                    datum = datum.decode('UTF-8')
                    # note sys.stdout won't actually get printed here due to buffering; sys.stdout.flush after the hg_method loop will display the whole thing
                    sys.stdout.write(f" : {datum}")
                # if .write gets a unicode error, take a look.
                except UnicodeEncodeError:
                    datum = datum.encode('UTF-8')
                    if DEBUG : print(f" : ENCODING ERROR! {datum}")
                    else : sys.stdout.write(f" : {datum}")
                    unicode_valid = False

            # append datum to working list, which will soon become a row in df_songs
            data.append(datum)
        
        # once all methods finished IF UNICODE IS VALID, append row to dataframe, and print if debug show what was appended
        if unicode_valid : df_songs = df_songs.append(pd.Series(data, index=df_songs.columns), ignore_index = True)
        if DEBUG : sys.stdout.flush()

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
filesize = sys.getsizeof(df_songs)
if DEBUG : print(f"-- sys.getsizeof(df_songs) [size in bytes]: {filesize} (= {filesize/1000000:.3f} mb)")

# Printing dataframe to csv via the save_df.py method, unless larger than 100mb; if we get a hellabig frame, we ought to split it up. 
if filesize < (100000000): save(df_songs, 'songs_df.csv')

# Separate file to facilitate simultaneous working/editing
df_songs = clean_columns(df_songs, DEBUG)

# Save again once cleaned, just because
if sys.getsizeof(df_songs) < (100000000): save(df_songs, 'cleaned_songs_df.csv')

# Running analysis!
graph(df_songs)