import re
data_in = input()

expression = r"\b_([a-zA-Z0-9]+)\b"
matches = re.findall(expression, data_in)
print(','.join(matches))

