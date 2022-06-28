cake_side_a = int(input())
cake_side_b = int(input())
cake = cake_side_a * cake_side_b
while cake > 0:
    user_input = input()
    if user_input == "STOP":
        break

    cake -= int(user_input)
if cake > 0:
    print(f"{cake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake)} pieces more.")
