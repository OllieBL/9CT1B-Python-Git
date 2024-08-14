# Import modules
import pandas as pd

y = []

# imports data
olympics_df = pd.read_csv('my files/Data analysis work/athlete_events.csv')
original_olympics_df = olympics_df

# data cleaning function
def clean():
    global olympics_df
    olympics_df.drop(columns=['Team', 'Year', 'Season', 'Sport'], inplace=True)

# data analysis function
def analyse(request):
    global olympics_df
    olympics_df = olympics_df[olympics_df[request['category']] == request['value']]
    if request['option'] == 'mean':
        for x in olympics_df:
            y.append(olympics_df[request['numRef']])
        
        
    

request = {
    'option' : 'mean',
    'category' : 'NOC',
    'value' : 'AUT',
    'numRef' : 'Age'
}
analyse(request)
