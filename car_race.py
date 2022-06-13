in_sequence = input().split()
left = 0
right = 0
for num in range(len(in_sequence) // 2):
    left += int(in_sequence[num])
    if int(in_sequence[num]) == 0:
        left = left * 0.8
for num in range(-1, -(len(in_sequence) // 2) + 1, -1):
    right += int(in_sequence[num])
    if int(in_sequence[num]) == 0:
        right = right * 0.8
if left < right:
    print(f"The winner is left with total time: {left:.1f}")
else:
    print(f"The winner is right with total time: {right:.1f}")
