line_in = input()

while not line_in == 'end':
    print(f"{line_in} = {line_in[::-1]}")

    line_in = input()
