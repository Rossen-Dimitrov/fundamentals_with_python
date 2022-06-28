price_vegetables  = float(input())
price_fruits  = float(input())
vegetables  = int(input())
fruits  = int(input())

total = (price_vegetables * vegetables + price_fruits * fruits) / 1.94
print(f'{total:.2f}')