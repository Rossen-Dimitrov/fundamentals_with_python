def odd_even_sum(number):
    even = 0
    odd = 0
    for value in number:
        if int(value) % 2 == 0:
            even += int(value)
        else:
            odd += int(value)
    return even, odd


input_nums = input()
even, odd = odd_even_sum(input_nums)
print(f"Odd sum = {odd}, Even sum = {even}")
