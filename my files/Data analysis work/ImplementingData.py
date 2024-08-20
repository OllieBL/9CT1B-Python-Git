# Import modules
import pandas as pd


# imports data
olympics_df = pd.read_csv('my files/Data analysis work/athlete_events.csv')
original_olympics_df = olympics_df
olympics_df = pd.DataFrame(olympics_df, index=['ID', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
# data cleaning function
def clean():
    global olympics_df
    olympics_df.drop(columns=['Team', 'Year', 'Season'], inplace=True)

# data analysis function

def analyse(request):
    meanList = []
    category = request['category']
    value = request['value']
    option = request['option']
    numRef = request['numRef']
    global olympics_df
    olympics_df = olympics_df[olympics_df[category] == value]
    olympics_df.dropna(subset=[request['numRef']])
    if option == 'mean':
        for index, row in olympics_df.iterrows():
           meanList.append(float(row[numRef]))
        mean = sum(meanList) / len(meanList)
        return mean
     
        
    

request = {
    'option' : 'mean',
    'category' : 'NOC',
    'value' : 'AUT',
    'numRef' : 'Age'
}
print(analyse(request))
