days = int(input())
room_type = str(input())
feedback = str(input())
price = 0
if room_type == "room for one person":
    price = 18.00
elif room_type == "apartment":
    price = 25
    if days < 10:
        price *= 0.7
    elif days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.5

elif room_type == "president apartment":
    price = 35
    if days < 10:
        price *= 0.9
    elif days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.80

total = (days - 1) * price
if feedback == "positive":
    total *= 1.25
    print(f"{total:.2f}")
else:
    total *= 0.9
    print(f"{total:.2f}")

