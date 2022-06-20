list_of_names = input().split(', ')
sorted_list_of_names = sorted(list_of_names, key=lambda item: (-len(item), item))
print(sorted_list_of_names)
