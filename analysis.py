# Import Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import hdf5_getters as hg

big_data = []
hg_methods = [
    hg.get_num_songs,
    hg.get_artist_familiarity,
    hg.get_duration,
    hg.get_title]

df_songs = pd.DataFrame(index =hg_methods) 
print(df_songs)
k = 0
count = 0
data = []
DEBUG = 1
test_length = 50
file_no = 0
#df_studies['proportion of red'] = redarray
#df_studies['proportion of red as percent'] = redpercentarray
#df_studies['proportion of blue area'] = bluearray
#df_studies['proportion of blue area as percent'] = bluepercentarray
#df_studies


# print(f'Target directory: {f'{os.getcwd()}/data/MillionSongSubset/data'} and type : {type(os.getcwd())}')


# Main loop to walk through all songs; uses users project install directory, but must be changed if we edit where the millionsong dataset is located
for subdir, dirs, files in os.walk(f'{os.getcwd()}/data/MillionSongSubset/data'):
    for file in files:

        hfile = hg.open_h5_file_read(os.path.join(subdir, file))

        for method in hg_methods:
            data.append(method(hfile))
            df_songs.head()   
#            df_songs = df_songs.append(pd.Series(data, index=df_songs.columns ), ignore_index=True)
#            print(data)
            data = []
        file_no +=1


        hfile.close()
        if (file_no > test_length) & (DEBUG == 1):
            break
    if (file_no > test_length) & (DEBUG == 1):
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



#h5 = hg.open_h5_file_read("data/MillionSongSubset/data/A/A/A/TRAAAAW128F429D538.h5")

# #duration = hg.get_duration(h5)
# #print(f'duration: {duration}')

# location = hg.get_artist_location(h5)
# print(f'location: {location}')

# num_songs = hg.get_num_songs(h5)
# print(f'num songs: {num_songs}')

# artist_name = hg.get_artist_name(h5)
# print(f'artist name: {artist_name}')
# print(type(artist_name))

# h5.close()
