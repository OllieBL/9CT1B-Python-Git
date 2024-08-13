# Import modules
import pandas as pd

# imports data
olympics_df = pd.read_csv('my files/Data analysis work/athlete_events.csv')

# data cleaning function
def clean():
    global olympics_df
    olympics_df.drop(columns=['Team', 'Year', 'Season', 'Sport'], inplace=True)

# 

clean()

