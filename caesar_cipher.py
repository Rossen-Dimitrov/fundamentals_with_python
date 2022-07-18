line_in = input()
encrypted_line = ''
for char in line_in:
    encrypted_line += chr(ord(char) + 3)
print(encrypted_line)
