import re
data_in = input()

expression = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"
matches = re.finditer(expression, data_in)
output = []

for match in matches:
    output.append(match.group())

print(' '.join(output))
