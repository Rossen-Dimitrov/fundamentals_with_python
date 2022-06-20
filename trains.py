num_wagons = int(input())
wagon_list = [0 for n in range(num_wagons)]
command = input()

while not command == "End":
    explode = command.split(" ")
    if explode[0] == "add":
        wagon_list[-1] += int(explode[1])
    elif explode[0] == "insert":
        wagon_list[int(explode[1])] += int(explode[2])
    elif explode[0] == "leave":
        wagon_list[int(explode[1])] -= int(explode[2])
    command = input()

print(wagon_list)
