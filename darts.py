player_name = str(input())
start_points = 301
successful_shots = 0
for shots in range(1, 300):
    target = str(input())
    if target == "Retire":
        print(f"{player_name} retired after {shots - successful_shots - 1} unsuccessful shots.")
        break
    points = int(input())
    if target == "Single":
        if (start_points - points) >= 0:
            start_points -= points
            successful_shots += 1
    elif target == "Double":
        if (start_points - points * 2) >= 0:
            start_points -= points * 2
            successful_shots += 1
    elif target == "Triple":
        if (start_points - points * 3) >= 0:
            start_points -= points * 3
            successful_shots += 1
    if start_points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break
