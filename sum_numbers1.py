total = 0

while True:
    user_input = input()
    if user_input == "NoMoreMoney":
        break
    elif float(user_input) < 0:
        print("Invalid operation!")
        break
    else:
        total += float(user_input)
        print(f"Increase: {float(user_input):.2f}")

print(f"Total: {total:.2f}")

# user_input = input()
#
# total = 0
#
# while user_input != "NoMoreMoney":
#
#     if float(user_input) < 0:
#         print("Invalid operation!")
#         break
#     else:
#         total += float(user_input)
#         print(f"Increase: {float(user_input):.2f}")
#         user_input = input()
# print(f"Total: {total:.2f}")



