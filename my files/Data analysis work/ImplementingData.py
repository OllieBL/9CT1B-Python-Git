# Import modules
import pandas as pd


# imports data
olympics_df = pd.read_csv('my files/Data analysis work/athlete_events.csv')
original_olympics_df = olympics_df
# data cleaning function
def clean():
    global olympics_df
    olympics_df.drop(columns=['Team', 'Games'], inplace=True)

# data analysis function
def analyse(request):
    category = request['category']
    value = request['value']
    option = request['option']
    numRef = request['numRef']
    global olympics_df
    olympics_df = olympics_df[olympics_df[category] == value]
    olympics_df.dropna(subset=[request['numRef']])
    if option == 'mean':
        mean = olympics_df[numRef].mean()
        return mean
    elif option == 'median':
        median = olympics_df[numRef].median()
        return median
     
        
    

request = {
    'option' : 'median',
    'category' : 'NOC',
    'value' : 'AUT',
    'numRef' : 'Height'
}
print(analyse(request))
request = {
    'option' : 'median',
    'category' : 'Year',
    'value' : 1992,
    'numRef' : 'Height'
}
print(analyse(request))
request = {
    'option' : 'median',
    'category' : 'Year',
    'value' : 2016,
    'numRef' : 'Height'
}
olympics_df = original_olympics_df
print(analyse(request))
request = {
    'option' : 'median',
    'category' : 'NOC',
    'value' : 'AUT',
    'numRef' : 'Height'
}
print(analyse(request))
