command = str(input())
new_list = command.split(", ")
counter = 0
start = len(new_list)
for i in range(start -1, -1, -1):
    if new_list[i] == "wolf" and counter == 0:
        print("Please go away and stop eating my sheep")
        break
    elif new_list[i] == "wolf":
        print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
    counter += 1

