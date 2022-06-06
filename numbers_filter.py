n = int(input())
even_list = []
odd_list = []
negative_list = []
positive_list = []

for num in range(n):
    filter_num = int(input())
    if filter_num % 2 == 0:
        even_list.append(filter_num)
    if not filter_num % 2 == 0:
        odd_list.append(filter_num)
    if filter_num < 0:
        negative_list.append(filter_num)
    if filter_num >= 0:
        positive_list.append(filter_num)
command = str(input())
if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "positive":
    print(positive_list)
else:
    print(negative_list)
