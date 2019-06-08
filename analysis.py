# Import Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import hdf5_getters as hg

hg_methods = [
    hg.get_num_songs,
    hg.get_artist_familiarity,
    hg.get_duration,
    hg.get_title]

# print(f'Target directory: {f'{os.getcwd()}/data/MillionSongSubset/data'} and type : {type(os.getcwd())}')


# Main loop to walk through all songs; uses users project install directory, but must be changed if we edit where the millionsong dataset is located
for subdir, dirs, files in os.walk(f'{os.getcwd()}/data/MillionSongSubset/data'):
    for file in files:

        hfile = hg.open_h5_file_read(os.path.join(subdir, file))

        hfile.close()


        print (
                f'Full: {os.path.join(subdir, file)}\n'
                f'subdir: {subdir}\n'
                f'file: {file}')


h5 = hg.open_h5_file_read("data/MillionSongSubset/data/A/A/A/TRAAAAW128F429D538.h5")

duration = hg.get_duration(h5)
print(f'duration: {duration}')

location = hg.get_artist_location(h5)
print(f'location: {location}')

num_songs = hg.get_num_songs(h5)
print(f'num songs: {num_songs}')

artist_name = hg.get_artist_name(h5)
print(f'artist name: {artist_name}')
print(type(artist_name))

h5.close()
