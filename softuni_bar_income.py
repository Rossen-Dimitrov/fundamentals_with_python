import re

pattern = r"^%(?P<customer>[A-Z][a-z]*)%[^|$%.]*<(?P<product>\w+)>[^|$%.]*\|(?P<count>[0-9]+)\|[^|$%.]*?" \
          r"(?P<price>[0-9]+\.*[0-9]*)\$$"

total = 0
text_in = input()
while not text_in == "end of shift":
    matches = re.search(pattern, text_in)
    if matches:
        customer = matches.group("customer")
        product = matches.group("product")
        count = int(matches.group("count"))
        price = float(matches.group("price"))
        current_price = price * count
        print(f"{customer}: {product} - {current_price:.2f}")
        total += current_price

    text_in = input()

print(f"Total income: {total:.2f}")
