minutes_day = int(input())
walks_day = int(input())
kilokal_day = int(input())

total_calories = minutes_day * walks_day * 5

if total_calories >= kilokal_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")

