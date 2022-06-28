import math

height = int(input())
width = int(input())
no_paint_percents = int(input())
painted = 0
square_maters_for_paint = math.ceil((height * width * 4) - ((height * width * 4) / 100) * no_paint_percents)

for n in range (2220):
    user_input = input()
    if user_input == "Tired!":
        print(f"{square_maters_for_paint - painted} quadratic m left.")
        break
    else:
        painted += int(user_input)
    if square_maters_for_paint == painted:
        print("All walls are painted! Great job, Pesho!")
        break
    if square_maters_for_paint < painted:
        print(f"All walls are painted and you have {painted - square_maters_for_paint} l paint left!")
        break
