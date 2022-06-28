number = int(input())
for n in range(1, number + 1):
    curr_num_as_str = str(n)
    current_sum = 0
    for num in curr_num_as_str:
        current_sum += int(num)
    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")


# number = int(input())
# for n in range(1, number + 1):
#     current_number = n
#     current_sum = 0
#     while current_number > 0:
#         current_sum += current_number % 10
#         current_number = current_number // 10
#     if current_sum == 5 or current_sum == 7 or current_sum == 11:
#         print(f"{n} -> True")
#     else:
#         print(f"{n} -> False")


