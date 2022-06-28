n_numbers = int(input())
p_2 = 0
p_3 = 0
p_4 = 0

for n in range(n_numbers):
    user_numbers = int(input())
    if user_numbers % 2 == 0 and user_numbers > 0:
        p_2 += 1
    if user_numbers % 3 == 0 and user_numbers > 0:
        p_3 += 1
    if user_numbers % 4 == 0 and user_numbers > 0:
        p_4 += 1
print(f"{(p_2 / n_numbers) * 100:.2f}%")
print(f"{(p_3 / n_numbers) * 100:.2f}%")
print(f"{(p_4 / n_numbers) * 100:.2f}%")