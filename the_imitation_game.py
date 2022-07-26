message = input()
instructions = input().split('|')

while not instructions[0] == "Decode":
    operations = instructions[0]
    if operations == 'Move':
        num = int(instructions[1])
        message = message[num:] + message[:num]
    elif operations == 'Insert':
        index = int(instructions[1])
        value = instructions[2]
        message = message[:index] + value + message[index:]
    elif operations == 'ChangeAll':
        substring = instructions[1]
        replacement = instructions[2]
        message = message.replace(substring, replacement)
    instructions = input().split('|')
print(f"The decrypted message is: {message}")
