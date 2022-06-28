needed_money = float(input())
owned_money = float(input())
spending_counter = 5
days_counter = 0
while True:
    save_or_spend = str(input())
    money = float(input())
    days_counter += 1
    if save_or_spend == "spend":
        owned_money -= money
        if owned_money < 0:
            owned_money = 0
        spending_counter -= 1
        if spending_counter == 0:
            print("You can't save the money.")
            print(f"{days_counter}")
            break
    if save_or_spend == "save":
        owned_money += money
        spending_counter = 5
    if owned_money >= needed_money:
        print(f"You saved the money for {days_counter} days.")
        break
