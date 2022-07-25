import re
data_in = input()
total = 0
expression = r"^>>(?P<furniture>[A-Za-z]+)<<(?P<price>[\d]+(\.[\d]+)?)!(?P<quantity>\d+)\b"

print("Bought furniture:")
while not data_in == "Purchase":
    match = re.search(expression, data_in)
    if match:
        furniture = match.group('furniture')
        price = float(match.group('price'))
        quantity = int(match.group('quantity'))
        total += quantity * price
        print(furniture)
    data_in = input()
print(f"Total money spend: {total:.2f}")
