def absolute_value():
    list_of_nums = input().split()
    abs_nums = []
    for n in list_of_nums:
        abs_nums.append(abs(float(n)))
    return abs_nums


print(absolute_value())
