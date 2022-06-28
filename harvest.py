import math

square_meter = int(input())
grape = float(input())
needed_liters = int(input())
workers = int(input())

for_wine = math.ceil((square_meter * grape * 0.4) / 2.5)
difference = abs(needed_liters - for_wine)

if for_wine < needed_liters:
    print(f"It will be a tough winter! More {math.ceil(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {for_wine} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(difference / workers)} liters per person.")