team_name = str(input())
games_played = int(input())
w_points = 0
d_points = 0
l_points = 0

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    for n in range(games_played):
        result = str(input())
        if result == "W":
            w_points += 3
        if result == "D":
            d_points += 1
        if result == "L":
            l_points += 1
    print(f"{team_name} has won {w_points + d_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {int(w_points / 3)}")
    print(f"## D: {d_points}")
    print(f"## L: {l_points}")
    print(f"Win rate: {((w_points / 3) / games_played) * 100:.2f}%")


