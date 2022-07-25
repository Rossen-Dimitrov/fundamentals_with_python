import re

data_in = input()
expression = r"\b(?P<day>\d{2})([/.-])(?P<month>[A-Z][a-z]{2})\2(?P<year>[\d]{4})\b"

matches = re.finditer(expression, data_in)
for match in matches:
    day = match.group("day")
    month = match.group("month")
    year = match.group("year")

    print(f"Day: {day}, Month: {month}, Year: {year}")
