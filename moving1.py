width = int(input())
length = int(input())
height = int(input())

total_cm = width * length * height

while total_cm > 0:
    user_input = input()
    if user_input == "Done":
        break
    total_cm -= int(user_input)
if total_cm > 0:
    print(f"{total_cm} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_cm)} Cubic meters more.")
