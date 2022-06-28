schedule = input().split(', ')

input_commands = input().split(':')
while not input_commands[0] == "course start":
    command = input_commands[0]
    lesson_title_1 = input_commands[1]
    if command == "Add":
        if lesson_title_1 not in schedule:
            schedule.append(lesson_title_1)

    elif command == "Insert":
        index = int(input_commands[2])
        if lesson_title_1 not in schedule and 0 <= index < len(schedule):
            schedule.insert(index, lesson_title_1)

    elif command == "Remove":
        if lesson_title_1 in schedule:
            schedule.remove(lesson_title_1)
            if lesson_title_1 + "-Exercise" in schedule:
                schedule.remove(lesson_title_1 + "-Exercise")

    elif command == "Swap":
        lesson_title_2 = input_commands[2]
        if lesson_title_1 in schedule and lesson_title_2 in schedule:
            first_index = schedule.index(lesson_title_1)
            second_index = schedule.index(lesson_title_2)
            schedule[first_index], schedule[second_index] = schedule[second_index], schedule[first_index]

            if lesson_title_1 + "-Exercise" in schedule:
                first = schedule.index(lesson_title_1 + "-Exercise")
                schedule.insert(second_index + 1, schedule.pop(first))
            if lesson_title_2 + "-Exercise" in schedule:
                second = schedule.index(lesson_title_2 + "-Exercise")
                schedule.insert(first_index + 1, schedule.pop(second))

    elif command == "Exercise":
        if lesson_title_1 in schedule and not lesson_title_1 + "-Exercise" in schedule:
            position = schedule.index(lesson_title_1)
            schedule.insert(position + 1, lesson_title_1 + "-Exercise")
        else:
            schedule.append(lesson_title_1)
            schedule.append(lesson_title_1 + "-Exercise")

    input_commands = input().split(':')

for position, lesson in enumerate(schedule):
    print(f'{position + 1}.{lesson}')
