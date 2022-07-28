string_in = input()
password = string_in

input_commands = input()

while not input_commands == "Done":
    input_commands = input_commands.split()
    command = input_commands[0]

    if command == "TakeOdd":
        temp_pass = password
        password = ''
        for i in range(len(temp_pass)):
            if not i % 2 == 0:
                password += temp_pass[i]
        print(password)

    elif command == "Cut":
        index = int(input_commands[1])
        length = int(input_commands[2])
        remove = password[index:(index + length)]
        password = password.replace(remove, '', 1)
        print(password)

    elif command == "Substitute":
        substring = input_commands[1]
        substitute = input_commands[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    input_commands = input()

print(f"Your password is: {password}")
