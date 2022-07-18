line_in = input()
explosion = 0
new_string = ''
for index, char in enumerate(line_in):
    if char == ">":
        explosion += int(line_in[index + 1])
        new_string += char
        continue
    if not char == ">" and explosion > 0:
        explosion -= 1
        continue
    else:
        new_string += char

print(new_string)
