command = input()
while command != "End":
    destination = command
    needed_money = float(input())
    saved_money = 0
    while saved_money < needed_money:
        current_sum = float(input())
        saved_money += current_sum
    print(f"Going to {destination}!" )
    command = input()

