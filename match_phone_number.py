import re
data = input()
pattern = r"\+359(\s|-)2\1\d{3}\1\d{4}\b"
matches = [obj.group() for obj in re.finditer(pattern, data)]

print(", ".join(matches))
