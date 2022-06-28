import sys

min_number = sys.maxsize
while True:
    user_input = input()
    if user_input == "Stop":
        print(min_number)
        break
    elif int(user_input) < min_number:
        min_number = int(user_input)