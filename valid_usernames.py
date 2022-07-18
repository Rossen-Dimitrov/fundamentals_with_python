line_in = input().split(', ')

for name in line_in:
    is_valid = True
    if 3 <= len(name) <= 16:
        if " " not in name:
            for char in name:
                if not (char.isalnum() or char == "_" or char == "-"):
                    is_valid = False
                    break
        else:
            is_valid = False
    else:
        is_valid = False
    if is_valid:
        print(name)


