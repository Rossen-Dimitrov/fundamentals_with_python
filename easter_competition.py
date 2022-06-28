number_of_breads = int(input())
max_name = ""
max_points = 0
for breads in range(number_of_breads):
    new_best_baker = False
    baker_name = str(input())
    current_points = 0
    while True:
        user_input = input()
        if user_input == "Stop":
            break
        current_points += int(user_input)
        if current_points > max_points:
            max_points = current_points
            max_name = baker_name
            new_best_baker = True
    print(f"{baker_name} has {current_points} points.")
    if new_best_baker:
        print(f"{baker_name} is the new number 1!")
print(f"{max_name} won competition with {max_points} points!")