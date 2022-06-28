term = str(input())
type_contract = str(input())
internet = str(input())
months = int(input())
price = 0

if term == "one":
    if type_contract == "Small":
        price = 9.98
    elif type_contract == "Middle":
        price = 18.99
    elif type_contract == "Large":
        price = 25.98
    elif type_contract == "ExtraLarge":
        price = 35.99
else:
    if type_contract == "Small":
        price = 8.58
    elif type_contract == "Middle":
        price = 17.09
    elif type_contract == "Large":
        price = 23.59
    elif type_contract == "ExtraLarge":
        price = 31.79

if internet == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

price = price * months

if term == "two":
    price *= 0.9625
    print(f"{price:.2f} lv.")
else:
    print(f"{price:.2f} lv.")