line_in = input().split()
str_1, str_2 = line_in
total_sum = 0

for index in range(0, len(max(line_in, key=len))):
    a = 0
    b = 0
    if not len(str_1) == len(str_2):
        if len(str_1) > len(str_2):
            a = ord(str_1[index])
            if index > len(str_2) - 1:
                b = 1
            else:
                b = ord(str_2[index])
        elif len(str_2) > len(str_1):
            b = ord(str_2[index])
            if index > len(str_1) - 1:
                a = 1
            else:
                a = ord(str_1[index])
    else:
        a = ord(str_1[index])
        b = ord(str_2[index])

    total_sum += a * b

print(total_sum)
