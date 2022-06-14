def add_and_subtract():
    nums_list = list(int(input()) for x in range(3))
    return (nums_list[0] + nums_list[1]) - nums_list[2]


print(add_and_subtract())
