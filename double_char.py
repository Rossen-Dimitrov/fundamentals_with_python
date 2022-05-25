while True:
    command = str(input())
    if command == "End":
        break
    elif command == "SoftUni":
        continue
    for char in command:
        print(char * 2, end="")
    print()

