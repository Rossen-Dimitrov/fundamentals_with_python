count_of_numbers = int(input())
even = 0
odd = 0

for numbers in range(count_of_numbers):
    current_num = int(input())
    if numbers % 2 == 0:
        even += current_num
    else:
        odd += current_num
diff = abs(even - odd)
if even == odd:
    print("Yes")
    print(f"Sum = {odd}")
else:
    print("No")
    print(f"Diff = {diff}")