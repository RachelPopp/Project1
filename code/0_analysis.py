# Import Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# grabbing the hdf5_getters.py file stored alongside analysis.py
# we use it to save us major time converting from the h5 files
# into a data format that we can use
import hdf5_getters as hg

# this step takes a little while, so, print
print('Done importing')

# Debug section; either True or False (1 or 0)
DEBUG = True
test_length = 50

# Collection of methods from hdf5_getters we want to use en masse
hg_methods = [
    hg.get_num_songs,
    hg.get_artist_familiarity,
    hg.get_duration,
    hg.get_title]

# Initializing datatypes we'll need later
big_data = []
df_songs = pd.DataFrame(index =hg_methods) 
print(df_songs)
k = 0
count = 0
data = []

file_no = 0


# print(f'Target directory: {f'{os.getcwd()}/data/MillionSongSubset/data'} and type : {type(os.getcwd())}')


# Main loop to walk through all songs; uses users project install directory, but must be changed if we edit where the millionsong dataset is located
for subdir, dirs, files in os.walk(f'{os.getcwd()}/../MillionSongSubset/data'):
    for file in files:

        hfile = hg.open_h5_file_read(os.path.join(subdir, file))

        # for method in hg_methods:
            # data.append(method(hfile))
            # df_songs.head()   
            # df_songs = df_songs.append(pd.Series(data, index=df_songs.columns ), ignore_index=True)
            # print(data)
            # data = []
        print(file_no)
        file_no +=1


        hfile.close()

        # exit file nested loop if we're in debug mode
        if (file_no > test_length) & DEBUG:
            break
    if (file_no > test_length) & DEBUG:
        break
#        if k > 1:
#            k = hg.get_num_songs(hfile)
#            print(k)
#            print(file)
#            break
#        count = count+1
#        print(count)
#        for method in hg_methods:
#            big_data.append(method)

        
#        duration = hg.get_duration(hfile)
#        print(f'duration: {duration}')
        

#        print (
 #               f'Full: {os.path.join(subdir, file)}\n'
 #               f'subdir: {subdir}\n'
  #              f'file: {file}')