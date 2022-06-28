tournament_name = input()
win_counter = 0
loss_counter = 0
while not tournament_name == "End of tournaments":
    games = int(input())
    for game_num in range(1, games + 1):
        desi_points = int(input())
        other_points = int(input())
        if desi_points > other_points:
            win_counter += 1
            print(f"Game {game_num} of tournament {tournament_name}: win with {desi_points - other_points} points.")
        else:
            loss_counter += 1
            print(f"Game {game_num} of tournament {tournament_name}: lost with {other_points - desi_points} points.")
    tournament_name = input()
wins = (win_counter / (win_counter + loss_counter)) * 100
loss = (loss_counter / (win_counter + loss_counter)) * 100
print(f"{wins:.2f}% matches win")
print(f"{loss:.2f}% matches lost")
