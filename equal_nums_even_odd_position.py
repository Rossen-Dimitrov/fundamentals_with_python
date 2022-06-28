first = int(input())
second = int(input())

for num in range(first, second + 1):
    odd_sum = 0
    even_sum = 0
    for current_num in range(len(str(num))):
        if current_num % 2 == 0:
            even_sum += int(str(num)[current_num])
        else:
            odd_sum += int(str(num)[current_num])

    if odd_sum == even_sum:
        print(num, end=" ")


# first_num = int(input())
# second_num = int(input())
#
# for number in range(first_num, second_num + 1):
#     even_sum = 0
#     odd_sum = 0
#     number_in_str = str(number)
#     for index, digit in enumerate(number_in_str):
#         if index % 2 ==0:
#             odd_sum += int(digit)
#         else:
#             even_sum += int(digit)
#     if odd_sum == even_sum:
#         print(number)