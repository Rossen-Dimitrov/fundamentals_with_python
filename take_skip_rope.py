string_skips = input()
numbers_list = []
non_numbers_list = []
take_list = []
skip_list = []
result_string = ''

for x in string_skips:
    if x.isdigit():
        numbers_list.append(int(x))
    else:
        non_numbers_list.append(x)
for index, value in enumerate(numbers_list):
    if index % 2 == 0:
        take_list.append(value)
    else:
        skip_list.append(value)
for num in range(len(take_list)):
    for char in range(take_list[num]):
        if len(non_numbers_list) > 0:
            result_string += non_numbers_list.pop(0)
    for char in range(skip_list[num]):
        if len(non_numbers_list) > 0:
            non_numbers_list.pop(0)

print(result_string)
