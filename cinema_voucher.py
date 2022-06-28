vouchers = int(input())
tickets = 0
others = 0

for n in range (2220):
    user_input = input()
    if user_input == "End":
        break
    elif len(user_input) > 8:
        purchase = ord(user_input[0]) + ord(user_input[1])
        if vouchers >= purchase:
            vouchers -= purchase
            tickets += 1
        else:
            break
    elif len(user_input) <= 8:
        purchase = ord(user_input[0])
        if vouchers >= purchase:
            vouchers -= purchase
            others +=1
        else:
            break
print(f"{tickets}")
print(f"{others}")
