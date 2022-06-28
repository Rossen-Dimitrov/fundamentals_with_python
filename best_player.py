player_name = input()
winner_name = ""
winner_score = 0
hat_trick = False
while player_name != "END":
    current_score = int(input())
    if current_score > 2:
        hat_trick = True
    if current_score > winner_score:
        winner_score = current_score
        winner_name = player_name
    if current_score > 9:
        break
    player_name = input()
if hat_trick:
    print(f"{winner_name} is the best player!")
    print(f"He has scored {winner_score} goals and made a hat-trick !!!")
else:
    print(f"{winner_name} is the best player!")
    print(f"He has scored {winner_score} goals.")

