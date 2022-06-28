sequence = input().split(' ')
count = 0
while True:
    command = input()
    if command == "End":
        break
    if 0 <= int(command) < len(sequence):
        count += 1
        sequence[int(command)] = str(-1)
        for num in sequence:
            if num > sequence[int(command)] != -1:
                sequence[int(command)] -= int(num)
            elif num < sequence[int(command)] != -1:
                sequence[int(command)] -= int(num)

print(f"Shot targets: {count} -> {' '.join(sequence)}")
