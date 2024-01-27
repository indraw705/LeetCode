country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# Do NOT change the code above 👆

# to be added to the travel_log.
dict01 = {}
def add_new_country(country, visits, list_of_cities):
    dict01["country"] = country
    dict01["visits"] = visits
    dict01["cities"] = list_of_cities
    travel_log.append(dict01)
    print(travel_log)


# Do not change the code below 👇


add_new_country("India", 4, ["Mumbai, Delhi, Goa"])
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
