def total_price():
    drink, quantity = str(input()), float(input())
    result = None
    if drink == 'coffee':
        result = quantity * 1.50
    elif drink == 'water':
        result = quantity * 1.00
    elif drink == 'coke':
        result = quantity * 1.40
    elif drink == 'snacks':
        result = quantity * 2.00
    return f'{result:.2f}'


print(total_price())
