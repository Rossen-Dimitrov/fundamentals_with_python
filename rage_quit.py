line_in = input().upper()
unique_symbols = set()
rage_message = ''
temp_message = ''
skip_this = False
for index, char in enumerate(line_in):
    if char.isdigit():
        if skip_this:
            skip_this = False
            continue
        if index + 1 <= len(line_in) - 1:
            if line_in[index + 1].isdigit():
                rage_message += temp_message * int(char + line_in[index + 1])
                temp_message = ''
                skip_this = True
            else:
                rage_message += temp_message * int(char)
                temp_message = ''
        else:
            rage_message += temp_message * int(char)
            temp_message = ''
    else:
        unique_symbols.add(char)
        temp_message += char

print(f"Unique symbols used: {len(unique_symbols)}\n{rage_message}")
