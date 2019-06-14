import os, csv

def save (df_songs, location):
    with open(os.path.join('..','code_output',location), 'w') as output_file:
        writer = csv.writer(output_file)
        df_songs.to_csv(output_file, encoding='utf-8')
        print(f"Saved to: {os.path.join('..','code_output',location)}")