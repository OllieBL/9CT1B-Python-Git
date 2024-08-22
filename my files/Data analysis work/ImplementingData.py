# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    plot = request['plot']
    global olympics_df

    olympics_df = olympics_df[olympics_df[category] == value]
    olympics_df.dropna(subset=[request['numRef']])
    if option == 'mean':
        mean = olympics_df[numRef].mean()
        output = mean
    elif option == 'median':
        median = olympics_df[numRef].median()
        output = median
    if plot == True:
        olympics_df.plot(
            kind='scatter',
            x='Year',
            y='Height',
            color='blue',
            alpha=0.3,
            title='Height over time for athletes'
            )
        z = np.polyfit(olympics_df['Year'], olympics_df['Height'], 1)
        p = np.poly1d(z)
        plt.plot(olympics_df['Year'], p(olympics_df['Year']))
        plt.show()
    return output
     
        
    

request = {
    'option' : 'median',
    'category' : 'NOC',
    'value' : 'AUT',
    'numRef' : 'Height',
    'plot' : True,
    'plotType' : 'scatter'
}
analyse(request)