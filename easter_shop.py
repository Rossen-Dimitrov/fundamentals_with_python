initial_eggs = int(input())
sold = 0
while True:
    user_input = str(input())
    if user_input == "Close":
        print("Store is closed!")
        print(f"{sold} eggs sold.")
        break
    eggs = int(input())
    if user_input == "Buy":
        if eggs > initial_eggs:
            print("Not enough eggs in store!")
            print(f"You can buy only {initial_eggs}.")
            break
        else:
            sold += eggs
            initial_eggs -= eggs
    elif user_input == "Fill":
        initial_eggs += eggs
