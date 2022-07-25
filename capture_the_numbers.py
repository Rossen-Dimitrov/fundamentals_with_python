import re

expression = r"\d+"
data_in = input()
matches = []
while True:
    if data_in:
        matches += re.findall(expression, data_in)
    else:
        break
    data_in = input()
print(' '.join(matches))
