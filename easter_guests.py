import math

guests = int(input())
budget = int(input())
egg = 0.45

eggs_count = guests * 2
egg_price = eggs_count * egg
easter_bread = math.ceil(guests / 3)

total = egg_price + easter_bread * 4
difference = abs(budget - total)

if budget >= total:
    print(f"Lyubo bought {easter_bread} Easter bread and {eggs_count} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")