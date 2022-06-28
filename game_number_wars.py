first_player = str(input())
second_player = str(input())
first_player_points = 0
second_player_points = 0

while True:
    input_pl_1 = input()
    if input_pl_1 == "End of game":
        print(f"{first_player} has {first_player_points} points")
        print(f"{second_player} has {second_player_points} points")
        break
    input_pl_2 = input()
    if int(input_pl_1) > int(input_pl_2):
        first_player_points += int(input_pl_1) - int(input_pl_2)
    elif int(input_pl_1) < int(input_pl_2):
        second_player_points += int(input_pl_2) - int(input_pl_1)
    elif int(input_pl_1) == int(input_pl_2):
        print("Number wars!")
        input_pl_1 = int(input())
        input_pl_2 = int(input())
        if input_pl_1 > input_pl_2:
            print(f"{first_player} is winner with {first_player_points} points")
            break
        else:
            print(f"{second_player} is winner with {second_player_points} points")
            break
