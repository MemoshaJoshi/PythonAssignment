# print the student name starting with 'r' in capital letter.
students = ['ram', 'sita', 'raman', 'rohit', 'gita']
"""
new_list = []
for student in students:
    if student[0] == 'r':
    new_list.append(student.upper)
"""

# list comprehension
new_list = [student.upper() for student in students if student[0] =='r']
print(new_list)

# dictionary
# wap to print the square of numbers from 1 to 10.

"""square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)"""

# dictionary comprehension
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)
