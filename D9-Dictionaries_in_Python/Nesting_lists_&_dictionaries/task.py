Capitals = {
    "France":"Paris",
    "Germany":"Berlin",
}

#Nested list in dictionaries
# travel_log = {
#     "France": ["Paris","Lille","Dijon"],
#     "SriLanka": ["Colombo","Ratnapura"],
# }

#Print lille
#print(travel_log["France"][1])

#List inside a list
#Accessing 'D'
# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])

#Dictionary inside a Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris","Lille","Dijon"],
        "num_times_visited": 2
    },
    "SriLanka": {
        "cities_visited": ["Colombo","Ratnapura"],
        "num_times_visited":5
    },
}

#Accessing Dijon
print(travel_log["France"]["cities_visited"][2])