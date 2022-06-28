user_name = input()
winner_name = " "
winner_points = 0

while user_name != "Stop":
    current_point = 0
    for letters in user_name:
        numbers = input()
        if int(numbers) == ord(letters):
            current_point += 10
        else:
            current_point += 2
        if current_point >= winner_points:
            winner_points = current_point
            winner_name = user_name
    user_name = input()
print (f"The winner is {winner_name} with {winner_points} points!")




