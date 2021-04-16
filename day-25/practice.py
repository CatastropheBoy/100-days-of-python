import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# # Get data in column
# print(data["temp"])
# print(data.temp.max())

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp_f = int(monday.temp) * 9/5 + 32
print(monday_temp_f)


some_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
panda_data = pandas.DataFrame(some_dict)
panda_data.to_csv("new_data.csv")
print(panda_data)