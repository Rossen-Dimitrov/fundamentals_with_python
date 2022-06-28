first = int(input())
second = int(input())
magic = int(input())
combination = 0
combination_exist = False
for num1 in range(first, second + 1):
    for num2 in range(first, second + 1):
        combination += 1
        if num1 + num2 == magic:
            combination_exist = True
            break
    if combination_exist:
        break
if combination_exist:
    print(f"Combination N:{combination} ({num1} + {num2} = {magic})")
else:
    print(f"{combination} combinations - neither equals {magic}")


# start_num = int(input())
# stop_num = int(input())
# magic_num = int(input())
# combination = 0
# condition = False
# for x1 in range(start_num, stop_num + 1):
#     for x2 in range(start_num, stop_num + 1):
#         combination += 1
#         if x1 + x2 == magic_num:
#             print(f"Combination N:{combination} ({x1} + {x2} = {magic_num})")
#             condition = True
#             break
#     if condition:
#         break
# if not condition:
#     print(f"{combination} combinations - neither equals {magic_num}")

