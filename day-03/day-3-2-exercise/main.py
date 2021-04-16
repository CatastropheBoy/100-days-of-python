# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height **2
print(f"Your BMI is {bmi}")
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal weight.")
elif bmi < 30:
    print("You are slightly overweight.")
elif bmi < 35:
    print("You are obsese.")
else:
    print("You are clinically obese")