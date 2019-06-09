import os, csv

def save (df_songs):
    with open(os.path.join('..','code_output','big_songs_df.csv'), 'w') as output_file:
        writer = csv.writer(output_file)
        # commented out following 2 lines until issue in unicode_save_issue.py is resolved
        # df_songs.to_csv(output_file, encoding='utf-8')
        # print(f"Saved to: {os.path.join('..','code_output','big_songs_df.csv')}")