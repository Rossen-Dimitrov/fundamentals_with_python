line_in = input().split()
alfa = "abcdefghijklmnopqrstuvwxyz"
total_sum = 0

for num in line_in:
    number = int(num[1:len(num) - 1])
    if num[0].isupper():
        letter_position = int(alfa.index(num[0].lower()) + 1)
        total_sum += number / letter_position
    if num[0].islower():
        letter_position = int(alfa.index(num[0]) + 1)
        total_sum += number * letter_position
    if num[-1].isupper():
        letter_position = int(alfa.index(num[-1].lower()) + 1)
        total_sum -= letter_position
    if num[-1].islower():
        letter_position = int(alfa.index(num[-1]) + 1)
        total_sum += letter_position

print(f"{total_sum:.2f}")
