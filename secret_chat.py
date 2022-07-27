message = input()

line_in = input()
while not line_in == "Reveal":
    line_in = line_in.split(":|:")
    command = line_in[0]
    if command == "InsertSpace":
        index = int(line_in[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif command == "Reverse":
        substring = line_in[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            message += substring[::-1]
            print(message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring, replacement = line_in[1], line_in[2]
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)
        else:
            print("error")
    line_in = input()
print(f"You have a new text message: {message}")
