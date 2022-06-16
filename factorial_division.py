import math


def factorial_div(first, second):
    first_result = math.factorial(first)
    second_result = math.factorial(second)

    return first_result / second_result


print(f'{factorial_div(int(input()), int(input())):.2f}')
