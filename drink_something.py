def print_drink(age):
    if age <= 14:
        return my_dict.get('kids')
    elif age <= 18:
        return my_dict.get('teens')
    elif age <= 21:
        return my_dict.get('young_adults')
    elif age > 21:
        return my_dict.get('adults')


my_dict = {"kids": "toddy", "teens": "coke", "young_adults": "beer", "adults": "whisky"}
age = int(input())
print(f'drink {print_drink(age)}')
