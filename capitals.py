countries = input().split(', ')
cities = input().split(', ')

countries_capitals = dict(zip(countries, cities))

for country, citi in countries_capitals.items():
    print(f"{country} -> {citi}")
