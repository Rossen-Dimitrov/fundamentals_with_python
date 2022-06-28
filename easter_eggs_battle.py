first_eggs = int(input())
second_eggs = int(input())
for n in range(200):
    user_input = str(input())
    if user_input == "End of battle":
        print(f"Player one has {first_eggs} eggs left.")
        print(f"Player two has {second_eggs} eggs left.")
        break
    if user_input == "one":
        second_eggs -= 1
    if user_input == "two":
        first_eggs -= 1
    if first_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_eggs} eggs left.")
        break
    elif second_eggs == 0:
        print(f"Player two is out of eggs. Player one has {first_eggs} eggs left.")
        break





