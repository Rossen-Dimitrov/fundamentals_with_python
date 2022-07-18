line_in = input()
new_line = ''
for index in range(0, len(line_in)):
    if index == len(line_in) - 1:
        new_line += line_in[-1]
    else:
        if not line_in[index] == line_in[index + 1]:
            new_line += line_in[index]

print(new_line)
