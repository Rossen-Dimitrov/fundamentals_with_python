import sys

n_numbers = int(input())
odd_max_number = -sys.maxsize
odd_min_number = sys.maxsize
even_max_number = -sys.maxsize
even_min_number = sys.maxsize
odd_sum = 0
even_sum = 0
condition_even = True
condition_odd = True
for n in range(1, n_numbers + 1):
    user_input = float(input())

    if n % 2 == 0:
        even_sum += user_input
        if user_input > even_max_number:
            even_max_number = user_input
        if user_input < even_min_number:
            even_min_number = user_input
    else:
        odd_sum += user_input
        if user_input > odd_max_number:
            odd_max_number = user_input
        if user_input < odd_min_number:
            odd_min_number = user_input
if (abs(odd_max_number) or odd_min_number) == sys.maxsize:
    condition_odd = False
if (abs(even_max_number) or even_min_number) == sys.maxsize:
    condition_even = False
if condition_odd:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min_number:.2f},")
    print(f"OddMax={odd_max_number:.2f},")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
if condition_even:
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min_number:.2f},")
    print(f"EvenMax={even_max_number:.2f}")
else:
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

