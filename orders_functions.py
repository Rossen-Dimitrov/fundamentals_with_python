def total_price():
    drink, quantity = str(input()), float(input())
    price = 0
    if drink == 'coffee':
        price = 1.50
    elif drink == 'water':
        price = 1.00
    elif drink == 'coke':
        price = 1.40
    elif drink == 'snacks':
        price = 2.00
    return f'{price * quantity:.2f}'


print(total_price())
