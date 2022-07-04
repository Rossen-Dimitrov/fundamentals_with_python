initial_loot = input().split('|')
steal_list = []
while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    else:
        if command[0] == 'Loot':
            for i in range(len(command)):
                item = command[i]
                if item not in initial_loot and i > 0:
                    initial_loot.insert(0, item)
        if command[0] == 'Drop':
            if 0 <= int(command[1]) < len(initial_loot):
                initial_loot.append(initial_loot.pop(int(command[1])))
        if command[0] == 'Steal':
            steal_list = initial_loot[- int(command[1]):]
            del initial_loot[- int(command[1]):]
            print(', '.join(steal_list))

if len(initial_loot) > 0:
    average_gain = 0
    for i in range(len(initial_loot)):
        average_gain += len(initial_loot[i])
    print(f"Average treasure gain: {average_gain / len(initial_loot):.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")
