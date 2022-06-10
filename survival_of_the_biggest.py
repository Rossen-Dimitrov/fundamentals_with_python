list_of_integers = list(map(int, (input().split())))
nums_to_remove = int(input())
for num in range(nums_to_remove):
    current_min = min(list_of_integers)
    list_of_integers.remove(current_min)
pr_list = map(str, list_of_integers)
print(', '.join(pr_list))
