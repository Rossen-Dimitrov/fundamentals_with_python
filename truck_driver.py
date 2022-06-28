season = str(input())
kilometers = float (input())
price = 0

if kilometers <= 5000:
    if season in "Spring Autumn":
        price = 0.75
    elif season == "Summer":
        price = 0.90
    elif season == "Winter":
        price = 1.05
elif 5000 < kilometers <= 10000:
    if season in "Spring Autumn":
        price = 0.95
    elif season == "Summer":
        price = 1.1
    elif season == "Winter":
        price = 1.25
elif 10000 < kilometers <= 20000:
    price = 1.45
total = (kilometers * price * 4) * 0.9
print(f"{total:.2f}")