# Import modules
import pandas as pd
import matplotlib.pyplot as plt

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
    Ref = request['Ref']
    plot = request['plot']
    global olympics_df
    counter = []

    if request['sort'] == True:
        olympics_df = olympics_df[olympics_df[category] == value]
    olympics_df.dropna(subset=[request['Ref']]) 
    checker = olympics_df
    if option == 'mean':
        mean = olympics_df[Ref].mean()
        output = mean
    elif option == 'median':
        median = olympics_df[Ref].median()
        output = median
    if plot == True:
        if type(olympics_df[Ref].values[0]) == int or type(olympics_df[Ref].values[0]) == float:
            checker =  pd.cut(olympics_df[Ref], 10, labels=False)
            print(checker)
        for i in checker[Ref].unique():
            c = checker[checker[Ref] == i]
            c = c[c['Medal'] == 'Gold']
            if len(c) != 0:
                counter.append(int(c['Medal'].value_counts()['Gold']))
            else:
                counter.append(0)
        dict = {'counter' : counter, 'sort' : checker.Height.unique()}
        df = pd.DataFrame(dict)
        df.sort_values(by=['counter'], ascending=False, inplace=True)
        df = df.head(10)
        plt.bar(df['sort'], df['counter'])
        plt.show()
    return output
     
def UI():
    while True:
        if input('calculations? True or False ') == True:
            option = input('median, mean, mode, max or minimum? ')
        if type(filter) != bool and type(option) == str:
            print('please enter a valid option')
        else:
            break
    while True:
        filter = input('Would you like to filter? True or False ')
        if type(filter) != bool:
            print('please enter a valid option')
        else:
            break
    while True:
        if filter == True:
            filter = input('What column to filter? Age, Height,  ')
            if type(filter) != bool:
                print('please enter a valid option')
            else:
                break

     

UI()