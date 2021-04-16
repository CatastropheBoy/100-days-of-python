programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

for i in programming_dictionary:
    print(programming_dictionary[i])

travel_log = [
    {
    "country": "France", 
    "cities_visited" : ["Paris", "Lille", "Dijon"], 
    "total_vists": 12,
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5,
    },
]
print(travel_log["France"]["cities_visited"])