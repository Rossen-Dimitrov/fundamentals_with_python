first_line_in = input()
targets = {}

while not first_line_in == "Sail":
    first_line_in = first_line_in.split("||")
    cities, population, gold = first_line_in[0], int(first_line_in[1]), int(first_line_in[2])

    if cities not in targets:
        targets[cities] = {"POP": 0, "GLD": 0}
    targets[cities]["POP"] += population
    targets[cities]["GLD"] += gold

    first_line_in = input()

second_line_in = input()

while not second_line_in == "End":
    second_line_in = second_line_in.split('=>')
    command, town = second_line_in[0], second_line_in[1]
    if command == "Plunder":
        people, gold = int(second_line_in[2]), int(second_line_in[3])
        targets[town]["POP"] -= people
        targets[town]["GLD"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if targets[town]["POP"] <= 0 or targets[town]["GLD"] <= 0:
            del targets[town]
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        gold = int(second_line_in[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            targets[town]["GLD"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {targets[town]['GLD']} gold.")
    second_line_in = input()

if targets:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    for town in targets:
        print(f'{town} -> Population: {targets[town]["POP"]} citizens, Gold: {targets[town]["GLD"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
