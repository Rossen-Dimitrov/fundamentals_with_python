integers_list = input().split(', ')
beggars = int(input())
collection = []
sum_bag = 0
for beggar in range(beggars):
    for num in integers_list[beggar::beggars]:
        sum_bag += int(num)
    collection.append(sum_bag)
    sum_bag = 0

print(collection)
