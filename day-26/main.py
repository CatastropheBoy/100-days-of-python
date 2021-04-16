import pandas
import random 
numbers = [1, 2, 3]
new_nums = [n + 1 for n in numbers]
print(new_nums)

name = "Angela"
new_list = [l for l in name]
print(new_list)

doubles = [n * 2 for n in range(1,5)]
print(doubles)

names = ['Alex', 'Beth', 'Dave', 'Eleanor', 'Freddie', 'Caroline']
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)

student_scores = {name:random.randint(1,100) for name in names}
print(student_scores)

passed_students = {student:score for student,score in student_scores.items() if score > 70}
print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)

for index, row in student_df.iterrows():
    print(row.student)