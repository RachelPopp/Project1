# Import Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import hdf5_getters as hg

test_length = 1000



hg_methods = [
    hg.get_num_songs,
    hg.get_artist_familiarity,
    hg.get_duration,
    hg.get_title]

# print(f'Target directory: {f'{os.getcwd()}/data/MillionSongSubset/data'} and type : {type(os.getcwd())}')

file_no = 0

# Main loop to walk through all songs; uses users project install directory, but must be changed if we edit where the millionsong dataset is located
for subdir, dirs, files in os.walk(f'{os.getcwd()}/data/MillionSongSubset/data'):
    for file in files:

        hfile = hg.open_h5_file_read(os.path.join(subdir, file))

        # checking for files with multiple songs; are none!
        if hg_methods[0](hfile) > 1:
            mult_song.append(file)
        
        print(f'#: {file_no} is titled: {hg_methods[3](hfile)}')

        hfile.close()

        file_no += 1
        if file_no > test_length:
            break
    if file_no > test_length:
        break
try:
    print(f'Multiple song file(s) is/are: {mult_song}')
except:
    print(f'No file with multiple songs!')