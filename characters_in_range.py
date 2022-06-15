def add_and_subtract():
    chars = list(input() for x in range(2))
    char_list = [chr(x) for x in range(ord(chars[0]) + 1, ord(chars[1]))]
    return char_list


print(' '.join(add_and_subtract()))
