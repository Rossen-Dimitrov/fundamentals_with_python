string_of_int = input().split(', ')
for num in string_of_int:
    if int(num) == 0:
        string_of_int.remove(num)
        string_of_int.append('0')
print(list(map(int, string_of_int)))
