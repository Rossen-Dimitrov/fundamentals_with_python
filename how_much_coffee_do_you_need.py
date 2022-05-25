command = str(input())
list_of_events = ["coding", "dog", "cat", "movie"]
coffee = 0
while not command == "END":
    if command.lower() in list_of_events:
        if command.islower():
            coffee += 1
        else:
            coffee += 2
    command = str(input())
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
