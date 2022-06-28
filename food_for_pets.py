days = int(input())
total_food = float(input())
total_food_eaten = 0
cat_total = 0
dog_total = 0
biscuits = 0

for day in range(1, days + 1):
    dog_eaten = int(input())
    dog_total += dog_eaten
    cat_eaten = int(input())
    cat_total += cat_eaten
    if day % 3 == 0:
        biscuits += (dog_eaten + cat_eaten) * 0.1
total_food_eaten = dog_total + cat_total
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{(total_food_eaten / total_food) * 100:.2f}% of the food has been eaten.")
print(f"{(dog_total / total_food_eaten) * 100:.2f}% eaten from the dog.")
print(f"{(cat_total / total_food_eaten) * 100:.2f}% eaten from the cat.")
