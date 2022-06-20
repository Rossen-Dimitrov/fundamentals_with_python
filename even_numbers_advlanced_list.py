list_of_nums = input().split(', ')
even_indexes = [index for index, num in enumerate(list_of_nums) if int(num) % 2 == 0]
print(even_indexes)
