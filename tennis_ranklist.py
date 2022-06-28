tournaments = int(input())
starting_points = int(input())
points = 0
wins = 0
for n in range(tournaments):
    game_stage = str(input())
    if game_stage == "W":
        points += 2000
        wins += 1
    if game_stage == "F":
        points += 1200
    if game_stage == "SF":
        points += 720
print(f"Final points: {starting_points + points}")
print(f"Average points: {int(points / tournaments)}")
print(f"{(wins / tournaments) * 100:.2f}%")
