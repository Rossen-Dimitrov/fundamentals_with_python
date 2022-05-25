def chat_codes(number):
    if number == 88:
        return "Hello"
    elif number == 86:
        return "How are you?"
    elif not (number == 88 or number == 86) and number < 88:
        return "GREAT!"
    elif number > 88:
        return "Bye."


numbers = int(input())
for num in range(numbers):
    print(chat_codes(int(input())))
