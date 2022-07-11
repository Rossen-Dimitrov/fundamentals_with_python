registered = {}
command = input()

while not command == "end":
    command = command.split(" : ")
    course = command[0]
    student = command[1]
    if course not in registered:
        registered[course] = []
    registered[course].append(student)

    command = input()
for courses, users in registered.items():
    print(f"{courses}: {len(users)}")
    for student in users:
        print(f"-- {student}")


