data_in = input().split(' ')

bakery_dict = {data_in[i]: int(data_in[i + 1]) for i in range(0, len(data_in), 2)}

print(bakery_dict)
