# fruits lists and hobbies

favourite_fruits = ['\napple', 'banana', 'orange']

# TODO: Add a new fruit to the list and print the result.
favourite_fruits.append('grape')
for fruit in favourite_fruits:
    print(fruit)

# TODO: Remove a fruit from the list and print the result.
favourite_fruits.pop(1)
for fruit in favourite_fruits:
    print(fruit)

# TODO: Change the order of fruits and print the result.
favourite_fruits = ['\ngrape', 'orange', 'apple']
for fruit in favourite_fruits:
    print(fruit)

# TODO: Access the second fruit in the list by index and print the result.
fruit = favourite_fruits[1]
print('\n', fruit)

# Custom List Manipulation Activity
#TODO: Create a list of favourite hobbies or activities
hobbies = ['reading', 'programming', 'playing games']

# TODO: Add a new hobby to the list and print the result
hobbies.append('hanging with friends')
for i in hobbies:
    print(i)

# TODO: Remove an existing hobby from the list and print the result
hobbies.pop('reading')
for i in hobbies:
    print(i)

# TODO: Change the order of hobbies and print the result
hobbies = ['programming', 'hanging with friends', 'playing games']
for i in hobbies:
    print(i)

# TODO: Update a specific hobby with a new one and print the result
hobbies[1] = 'reading'
for i in hobbies:
    print(i)