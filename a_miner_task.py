from collections import defaultdict
item = str(input())
item_dict = defaultdict(int)

while not item == 'stop':
    value = int(input())
    item_dict [item] += value

    item = str(input())

for item, count in item_dict.items():
    print(f"{item} -> {count}")
