def min_max_and_sum(nums):
    min_num = min(nums)
    max_num = max(nums)
    sum_num = sum(nums)
    return min_num, max_num, sum_num


num_in = list(map(int, input().split()))
min_num, max_num, sum_num = min_max_and_sum(num_in)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_num}")
