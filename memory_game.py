sequence_elements = list(input().split(' '))
command = input()
num_of_moves = 0
while True:
    if command == 'end' or len(sequence_elements) == 0:
        break
    else:
        indexes = command.split(' ')
        number_1 = int(indexes[0])
        number_2 = int(indexes[1])
        num_of_moves += 1
        if 0 <= number_1 <= (len(sequence_elements) - 1) and 0 <= number_2 <= (len(sequence_elements) - 1) and \
                number_1 != number_2:
            if sequence_elements[number_1] == sequence_elements[number_2]:
                print(f"Congrats! You have found matching elements - {sequence_elements[number_1]}!")
                sequence_elements.pop(max(number_1, number_2))
                sequence_elements.pop(min(number_1, number_2))

            else:
                print("Try again!")
        else:
            sequence_elements.insert(len(sequence_elements) // 2, f"-{num_of_moves}a")
            sequence_elements.insert(len(sequence_elements) // 2, f"-{num_of_moves}a")
            print("Invalid input! Adding additional elements to the board")
    command = input()

if len(sequence_elements) == 0:
    print(f"You have won in {num_of_moves} turns!")
else:
    print("Sorry you lose :(")
    print(' '.join(sequence_elements))

