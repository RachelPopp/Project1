# Import Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import hdf5_getters as hg

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
