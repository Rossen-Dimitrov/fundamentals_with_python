days = int(input())
room_type = input()
rating = input()
price = 0

if room_type == "room for one person":
    price = 18.00
elif room_type == "apartment":
    if days < 10:
        price = 0.7 * 25
    elif days < 15:
        price = 0.65 * 25
    else:
        price = 0.5 * 25
elif room_type == "president apartment":
    if days < 10:
        price = 0.9 * 35
    elif days < 15:
        price = 0.85 * 35
    else:
        price = 0.8 * 35
if rating == "positive":
    price *= 1.25
else:
    price *= 0.9
total = price * (days - 1)
print(f"{total:.2f}")