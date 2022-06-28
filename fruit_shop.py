product = input()
day_of_week = input()
quantity = float(input())
condition = True

if day_of_week in "Monday Tuesday Wednesday Thursday Friday":
    if product == "banana":
        price = 2.5
    elif product == "apple":
        price = 1.2
    elif product == "orange":
        price = 0.85
    elif product == "grapefruit":
        price = 1.45
    elif product == "kiwi":
        price = 2.7
    elif product == "pineapple":
        price = 5.5
    elif product == "grapes":
        price = 3.85
else:
    condition = False

if day_of_week in "Saturday Sunday":
    if product == "banana":
        price = 2.7
    elif product == "apple":
        price = 1.25
    elif product == "orange":
        price = 0.9
    elif product == "grapefruit":
        price = 1.6
    elif product == "kiwi":
        price = 3
    elif product == "pineapple":
        price = 5.6
    elif product == "grapes":
        price = 4.2
else:
    condition = False

if condition:
    print(f'{quantity * price:.2f}')
else:
    print("error")
