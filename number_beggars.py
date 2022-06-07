integers_list = input().split(', ')
beggars = int(input())
collection = []
for beggar in range(beggars):
    sum_bag = 0
    for num in integers_list[beggar::beggars]:
        sum_bag += int(num)
    collection.append(sum_bag)

print(collection)
