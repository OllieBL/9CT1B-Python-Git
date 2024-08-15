# Import modules
import pandas as pd

meanList = []

# imports data
olympics_df = pd.read_csv('my files/Data analysis work/athlete_events.csv')
original_olympics_df = olympics_df
olympics_df = pd.DataFrame(index=[range(len(olympics_df))])
# data cleaning function
def clean():
    global olympics_df
    olympics_df.drop(columns=['Team', 'Year', 'Season'], inplace=True)

# data analysis function
def analyse(request):
    global olympics_df
    olympics_df = olympics_df[olympics_df[request['category']] == request['value']]
    olympics_df.dropna(subset=[request['numRef']])
    if request['option'] == 'mean':
        for i in range(len(olympics_df)):
            meanList.append(olympics_df.iloc[3][i])
        mean = sum(meanList) / len(meanList)
        return mean
        
        
    

request = {
    'option' : 'mean',
    'category' : 'NOC',
    'value' : 'AUT',
    'numRef' : 'Age'
}
print(analyse(request))
