sequence = list(map(int, input().split(', ')))
group = 10
while len(sequence) > 0:
    temp_list = []
    for nums in sequence:
        if nums <= group:
            temp_list.append(nums)
    for nums in sequence[::-1]:
        if nums <= group:
            sequence.remove(nums)
    print(f"Group of {group}'s: {temp_list}")
    group += 10
