month = input()
nights = int(input())
price_st = 0
price_ap = 0

if month in "May October":
    price_st = 50
    price_ap = 65
    if 7 < nights <= 14:
        price_st *= 0.95
    elif nights > 14:
        price_st *= 0.7
        price_ap *= 0.9
elif month in "June September":
    price_st = 75.2
    price_ap = 68.7
    if nights > 14:
        price_st *= 0.8
        price_ap *= 0.9
elif month in "July August":
    price_st = 76
    price_ap = 77
    if nights > 14:
        price_ap *= 0.9

print(f"Apartment: {price_ap * nights:.2f} lv.")
print(f"Studio: {price_st * nights:.2f} lv.")