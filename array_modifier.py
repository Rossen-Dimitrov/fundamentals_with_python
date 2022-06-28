nums = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == 'end':
        print(', '.join(map(str, nums)))
        break
    elif command[0] == 'swap':
        nums[int(command[1])], nums[int(command[2])] = nums[int(command[2])], nums[int(command[1])]
    elif command[0] == 'multiply':
        nums[int(command[1])] *= nums[int(command[2])]
    elif command[0] == 'decrease':
        nums = [x - 1 for x in nums]
    user_input = input().split()
