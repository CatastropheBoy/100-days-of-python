
with open("file1.txt") as f:
    list_1 = f.readlines()

with open("file2.txt") as f:
    list_2 = f.readlines()

result = [int(n) for n in list_1 if n in list_2]
# Write your code above 👆

print(result)


