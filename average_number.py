user_in = int(input())
total = 0
for n in range(user_in):
    new_nums = int(input())
    total += new_nums
print(f"{total / user_in:.2f}")