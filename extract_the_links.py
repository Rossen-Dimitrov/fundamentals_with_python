import re
data_in = input()
expression = r"(w{3}.[-A-Za-z0-9]+(\.[a-z]+)+)"

while data_in:
    match = re.search(expression, data_in)
    if match:
        print(match.group(0))
    data_in = input()
