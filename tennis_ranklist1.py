tournament = int(input())
starting_points = int(input())
points = 0
win = 0
for _ in range(tournament):
    stage = input()
    if stage == "W":
        points += 2000
        win += 1
    elif stage == "F":
        points += 1200
    elif stage == "SF":
        points += 720
print(f"Final points: {starting_points + points}")
print(f"Average points: {int(points / tournament)}")
print(f"{(win / tournament) * 100:.2f}%")
