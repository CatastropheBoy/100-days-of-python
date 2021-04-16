# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
average_height = 0
students = 0
for i in student_heights:
    average_height += i
    students += 1
average_height = round(average_height / students)
print(average_height)
