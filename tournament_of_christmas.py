days = int(input())
win_counter = 0
lose_counter = 0
day_profit = 0
total = 0
for d in range(days):
    command = str(input())
    day_profit = 0
    day_win_counter = 0
    day_lose_counter = 0
    while command != "Finish":
        if command == "win":
            win_counter += 1
            day_profit += 20
            day_win_counter += 1
        elif command == "lose":
            lose_counter += 1
            day_lose_counter += 1
        command = str(input())
    if day_win_counter > day_lose_counter:
        day_profit *= 1.1
        total += day_profit
    else:
        total += day_profit

if win_counter > lose_counter:
    total *= 1.2
    print(f"You won the tournament! Total raised money: {total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total:.2f}")

