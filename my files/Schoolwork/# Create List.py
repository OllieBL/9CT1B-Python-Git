# Create List
student = {'name': 'Ollie', 'age': 14, 'suburb': 'Terrigal'}

# Access 'name' and 'age' keys
print(student['name'])
print(student['age'])

# Change suburb value
student['suburb'] = 'Gosford'

# Add email
student['email'] = 'oliver.black4@education.nsw.gov.au'

# Remove age
del student['age']

# Iterate and print keys
for key, value in student.items():
    print(key)

# Iterate and print values and keys
for key, value in student.items():
    print(key, value)

# Check for email
if 'email' in student:
    print('email key exists')
else:
    print('email key does not exist')