stage = str(input())
ticket_type = str(input())
number_tickets = int(input())
picture = str(input())
price = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        price = 55.5
    elif ticket_type == "Premium":
        price = 105.20
    elif ticket_type == "VIP":
        price = 118.9
elif stage == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.4
else:
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400

price = number_tickets * price
total = price
if price > 4000:
    total *= 0.75
elif price >= 2500:
    total *= 0.90
if picture == "Y" and price <= 4000:
    total += 40 * number_tickets

print(f"{total:.2f}")
