import pandas

squirrel_census = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(squirrel_census)


cinnamon_count = len(squirrel_census[squirrel_census["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_census[squirrel_census["Primary Fur Color"] == "Black"])
gray_count = len(squirrel_census[squirrel_census["Primary Fur Color"] == "Gray"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")