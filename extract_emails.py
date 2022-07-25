import re
data_in = input()

expression = r"(?<=\s)(([a-z0-9]+[a-z0-9\._\-]*)@[a-z\-]+(\.[a-z]+)+)\b"
matches = re.findall(expression, data_in)
for match in matches:
    print(match[0])