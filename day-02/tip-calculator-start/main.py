#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
bill = float(input("How much is the bill?\n"))
people = int(input("How many people are splitting the bill?\n"))
tip = round(float(input("How percentage is the tip?\n")) / 100 + 1, 2)
share = round((bill * tip) / people, 2)
print (f"With a bill of ${bill}, and a tip of {round((tip - 1) * 100)}%, each of the {people} people should pay: ${share}")