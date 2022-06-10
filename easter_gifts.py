gift_list = input().split()

command_in = input()
while not command_in == "No Money":
    command = command_in.split()
    if command[0] == 'OutOfStock' and command[1] in gift_list:
        for index in range(len(gift_list)):
            if gift_list[index] == command[1]:
                gift_list[index] = "None"

    elif command[0] == 'Required' and int(command[2]) in range(len(gift_list)):
        gift_list[int(command[2])] = command[1]

    elif command[0] == 'JustInCase':
        gift_list[-1] = command[1]
        
    command_in = input()

print(" ".join( x for x in gift_list if not x == "None"))
