input_nums = input().split()
string_in = input()
message = ''
for num in input_nums:
    index = 0
    for n in num:
        index += int(n)
    while index > len(string_in):
        index = index - len(string_in)
    message += string_in[index]
    string_in = string_in[:index] + string_in[index + 1:]
print(message)
