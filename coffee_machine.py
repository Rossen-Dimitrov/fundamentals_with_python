drink_type = input()
sugar = input()
drinks_amount = int(input())
price = 0
if drink_type == "Espresso":
    if sugar == "Without":
        price = 0.9 * 0.65
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.2
    if drinks_amount >= 5:
        price *= 0.75
elif drink_type == "Cappuccino":
    if sugar == "Without":
        price = 1 * 0.65
    elif sugar == "Normal":
        price = 1.2
    elif sugar == "Extra":
        price = 1.6
elif drink_type == "Tea":
    if sugar == "Without":
        price = 0.5 * 0.65
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7

total = drinks_amount * price

if total > 15:
    total *= 0.80
print(f"You bought {drinks_amount} cups of {drink_type} for {total:.2f} lv.")