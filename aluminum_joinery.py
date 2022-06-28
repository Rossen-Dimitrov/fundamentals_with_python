amount = int(input())
type_1 = str(input())
delivery = str(input())
price = 0

if amount < 10:
    print("Invalid order")
    exit()

if type_1 == "90X130":
    if amount < 30:
        price = 110
    elif 30 < amount < 60:
        price = 110 * 0.95
    else:
        price = 110 * 0.92
elif type_1 == "100X150":
    if amount < 40:
        price = 140
    elif 40 < amount < 80:
        price = 140 * 0.94
    else:
        price = 140 * 0.90
elif type_1 == "130X180":
    if amount < 20:
        price = 190
    elif 20 < amount < 50:
        price = 190 * 0.93
    else:
        price = 190 * 0.88
elif type_1 == "200X300":
    if amount <= 25:
        price = 250
    elif 25 < amount <= 50:
        price = 250 * 0.91
    else:
        price = 250 * 0.86

total_price = amount * price

if delivery == "With delivery":
    total_price += 60
elif delivery == "Without delivery":
    total_price = total_price

if amount > 99:
    total_price *= 0.96

print(f"{total_price:.2f} BGN")
