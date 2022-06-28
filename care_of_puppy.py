food = int(input())
food *= 1000
user_input = input()
eaten_food = 0

while user_input != "Adopted":
    eaten_food += int(user_input)
    user_input = input()
diff = abs(food - eaten_food)
if food >= eaten_food:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")