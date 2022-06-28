capacity = int(input())
incomes = 0
people = 0
condition = True
for n in range(200):
    user_input = input()
    if user_input == "Movie time!" or capacity == 0:
        print(f"There are {capacity - people} seats left in the cinema.")
        print(f"Cinema income - {incomes} lv.")
        break
    if int(user_input) % 3 == 0:
        people += int(user_input)
        if people > capacity:
            condition = False
            break
        else:
            incomes += (int(user_input) * 5) - 5
    else:
        people += int(user_input)
        if people > capacity:
            condition = False
            break
        else:
            incomes += int(user_input) * 5
if not condition:
    print("The cinema is full.")
    print(f"Cinema income - {incomes} lv.")