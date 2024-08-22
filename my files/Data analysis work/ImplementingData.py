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
    counter = []

    #olympics_df = olympics_df[olympics_df[category] == value]
    olympics_df.dropna(subset=[request['numRef']])
    if option == 'mean':
        mean = olympics_df[numRef].mean()
        output = mean
    elif option == 'median':
        median = olympics_df[numRef].median()
        output = median
    if plot == True:
        for i in olympics_df.NOC.unique():
            c = olympics_df[olympics_df['NOC'] == i]
            c = c[c['Medal'] == 'Gold']
            if len(c) != 0:
                counter.append(int(c['Medal'].value_counts()['Gold']))
            else:
                counter.append(0)
        print(counter)
        plt.bar(olympics_df.NOC.unique(),counter)
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