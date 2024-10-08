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
    plot = bool(request['plot'])
    output = 0
    global olympics_df
    counter = []

    if bool(request['sort']) == True:
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
        checker = olympics_df
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
        dict = {'counter' : counter, 'sort' : pd.unique(checker[Ref])}
        df = pd.DataFrame(dict)
        df.sort_values(by=['counter'], ascending=False, inplace=True)
        df = df.head(10)
        plt.bar(df['sort'], df['counter'])
        plt.show()
    return output
     
def UI():
    check = ''
    option = ''
    filter = ''
    category = ''
    value = ''
    
    global olympics_df
    while True:
        check = input('calculations? True or False ')
        if check == 'True':
            option = input('median or mean? ')
            if option == 'median' or option == 'mean' :
                break
            else:
                print('please enter a valid option')
        else:
            break
    while True:
        filter = input('Would you like to filter? True or False ')
        if filter == 'True' or filter == 'False':
            break
        else:
            print('please enter a valid option')
    while True:
        if filter == 'True':
            category = input('What column to filter? Age, Sex, Sport, NOC or Event')
            if category == 'Age' or category == 'Sport' or category == 'Event' or category == 'NOC':
                break
            else:
                print('please enter a valid option')
        else:
            break
    while True:
        if filter == 'True' and type(category) == str:
            value = input('What value do you want to sort with? ')
            break
        else:
            break
    while True: 
        Ref = input('what column do you want the data to display with? Sex, Age, Height, Weight, NOC, Sport or Event? ')
        if Ref == 'Age' or Ref == 'Sport' or Ref == 'Event' or Ref == 'Sex' or Ref == 'NOC'or Ref == 'Height' or Ref == 'Weight':
            break
        else:
            print('please enter a valid option')
    while True:
        plot = input('do you want a plot? True or False ')
        if plot == 'True' or plot == 'False':
            break
        else:
            print('please enter a valid option')
    request = {
        'option' : option,
        'category' : category,
        'value' : value,
        'plot' : plot,
        'Ref' : Ref,
        'sort' : filter
    }
    x = analyse(request)
    if check == True:
        print(x)
        

     

UI()