# make a dictionary
# take inputs
name = input('what is your name? ')
age = input('what is you age? ')
favsub = input('what is your favourite subject? ')

# make the dictionary
student = {'name': name, 'age': age, 'favourite subject': favsub}

# print out dictionary
for key, value in  student.items():
    print(key, value)