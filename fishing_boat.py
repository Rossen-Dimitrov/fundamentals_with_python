budget = int(input())
season = input()
fishers = int(input())
price = 0

if season == "Spring":
    price = 3000
    if fishers <= 6:
        price *= 0.9
    elif fishers <= 11:
        price *= 0.85
    elif fishers > 11:
        price *= 0.75
elif season == "Summer" or season == "Autumn":
    price = 4200
    if fishers <= 6:
        price *= 0.9
    elif fishers <= 11:
        price *= 0.85
    elif fishers > 11:
        price *= 0.75
elif season == "Winter":
    price = 2600
    if fishers <= 6:
        price *= 0.9
    elif fishers <= 11:
        price *= 0.85
    elif fishers > 11:
        price *= 0.75

if fishers % 2 == 0 and season != "Autumn":
    price *= 0.95

difference = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")