def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(sums, num_3):
    return sums - num_3


def add_and_subtract(first_, second_, third_):
    return subtract(sum_numbers(first_, second_), third_)


first = int(input())
second = int(input())
third = int(input())
print(add_and_subtract(first, second, third))


