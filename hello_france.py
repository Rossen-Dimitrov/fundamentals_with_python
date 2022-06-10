def check_price(types, price):
    if types == 'Clothes' and price <= 50:
        return True
    elif types == 'Shoes' and price <= 35:
        return True
    elif types == 'Accessories' and price <= 20.5:
        return True


collection = input().split('|')
budget = float(input())
bought_items = []
profit = 0

for items in collection:
    items = items.split('->')
    type_of_item = items[0]
    price_of_item = float(items[1])
    if check_price(type_of_item, price_of_item) and budget - price_of_item >= 0:
        budget -= price_of_item
        bought_items.append(f"{price_of_item * 1.4:.2f}")
        profit += price_of_item * 0.4
print(" ".join(bought_items))
print(f'Profit: {profit:.2f}')
if sum(map(float, bought_items)) + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
