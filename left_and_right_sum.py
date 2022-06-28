user_input = int(input())
left_sum = 0
right_sum = 0
for numbers in range(2 * user_input):
    current_num = int(input())
    if numbers < user_input:
        left_sum += current_num
    else:
        right_sum += current_num
diff = abs(left_sum - right_sum)
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")