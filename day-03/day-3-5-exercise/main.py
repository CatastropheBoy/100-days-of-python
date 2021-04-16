# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
love_count1 = 0
love_count2 = 0
couple = name1.upper() + name2.upper()
love_count1 += couple.count("T")
love_count1 += couple.count("R")
love_count1 += couple.count("U")
love_count1 += couple.count("E")
love_count2 += couple.count("L")
love_count2 += couple.count("O")
love_count2 += couple.count("V")
love_count2 += couple.count("E")
love_count = (love_count1 * 10) + love_count2
print(f"Your love score is {love_count}.")
if love_count < 10 or love_count > 90:
    print("You go together like coke and mentos.")
elif love_count < 50 and love_count > 40:
    print("You are alright together.")
else:
    print("Whatever.")

