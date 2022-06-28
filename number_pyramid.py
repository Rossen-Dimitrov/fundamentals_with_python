user_input = int(input())
counter = 1
for row in range(0, user_input):
    for colons in range(0, row + 1):
        if counter <= user_input:
            print(counter, end=" ")
            counter += 1
    print()


# user_input = int(input())
# counter = 1
# all_is_printed = False
# for raw in range(1, user_input + 1):
#     for nums in range(1, raw + 1):
#         print(counter, end=" ")
#         counter += 1
#         if counter > user_input:
#             all_is_printed = True
#             break
#
#     if all_is_printed:
#         break
#     print()

