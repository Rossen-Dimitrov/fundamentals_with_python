def rounding(nums):
    rounded = []
    for n in nums:
        rounded.append(round(float(n)))
    return rounded


user_input = input().split()
print(rounding(user_input))
