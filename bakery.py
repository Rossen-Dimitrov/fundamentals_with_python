data_input = input().split(' ')
bakery_dict = {}
for index in range(0, len(data_input), 2):
    bakery_dict[data_input[index]] = int(data_input[index + 1])

print(bakery_dict)
