import math

days = int(input())
food_kg = int(input())
food_day_dog = float(input())
food_day_cat = float(input())
food_day_turtle = float(input()) / 1000

total = math.ceil((food_day_dog + food_day_cat + food_day_turtle) * days)
diff = abs(total - food_kg)
if total <= food_kg:
    print(f"{diff} kilos of food left.")
else:
    print(f"{diff} more kilos of food are needed.")