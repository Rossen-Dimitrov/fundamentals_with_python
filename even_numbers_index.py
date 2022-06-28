# user_input = list(map(int, input().split(", ")))
# found_indices = map(lambda x: x if user_input[x] % 2 == 0 else 'no', range(len(user_input)))
# even_indices = list(filter(lambda a: a != 'no', found_indices))
# print(even_indices)


# even_list = []
# user_input = input().split(", ")
# for num in range(len(user_input)):
#     if int(user_input[num]) % 2 == 0:
#         even_list.append(num)
# print(even_list)

even_list = []
user_input = input().split(", ")
even_list += [num for num in range(len(user_input)) if int(user_input[num]) % 2 == 0]
print(even_list)