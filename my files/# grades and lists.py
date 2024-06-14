# grades and lists
# Create lists for student names and grades
student_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
student_grades = [85, 92, 78, 88, 95]

#TODO: Add a new student and their grade to the lists
student_names.append('Chris')
student_grades.append(89)

#TODO: Print the original lists
print(student_names[:5])
print(student_grades[:5])

#TODO: Remove the third student and their grade from the list
student_names.pop(2)
student_grades.pop(2)

#TODO: Print the updated lists after removal
print(student_names)
print(student_grades)

#TODO: Update the grade of a specific student
student_grades[1] = 75

#TODO: Calculate and print the average grade of all students
sum = 0
for x in student_grades:
    sum += x
average = sum / len(student_grades)
print(average)