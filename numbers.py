numbers = list(map(int, (input().split(' '))))
sorted_list = sorted(numbers, key=lambda x: -x)
list_to_be_printed = []

for num in range(len(sorted_list)):
    if sorted_list[num] > sum(sorted_list) / len(sorted_list):
        list_to_be_printed.append(sorted_list[num])

if len(list_to_be_printed) == 0:
    print("No")
else:
    print(*list_to_be_printed[:5])
