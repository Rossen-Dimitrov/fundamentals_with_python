def filter_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


numbers = map(int, input().split())
even_numbers = list(filter(filter_even, numbers))
print(even_numbers)
