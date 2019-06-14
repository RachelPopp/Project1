import os, csv

# Just saving a given df to given filename; relative location fixed
def save (df_songs, filename):
    with open(os.path.join('..','code_output',filename), 'w') as output_file:
        writer = csv.writer(output_file)
        
        # Save... if it works.
        try:
            df_songs.to_csv(output_file, encoding='utf-8')
            # little confirmation message when done saving
            print(f"Saved to: {os.path.join('..','code_output',filename)}")
        except:
            # If an error, say so and print what it was
            print(f"ERROR! 'df_songs' NOT SAVED TO {filename}")
            print(f"Error type: {sys.exc_info()[0]}")