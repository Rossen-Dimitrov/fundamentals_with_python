user_input = input().split("|")
budget = int(input())
condition = False
type_of_item = []
price_of_item = 0
profit = 0
total = 0
for item in user_input:
    splitted_item = item.split("->")
    type_of_item = splitted_item[0]
    price_of_item = float(splitted_item[1])
    condition = False
    if type_of_item == "Clothes" and price_of_item <= 50:
        condition = True
    elif type_of_item == "Shoes" and price_of_item <= 35:
        condition = True
    elif type_of_item == "Accessories" and price_of_item <= 20.50:
        condition = True

    if condition and budget - price_of_item >= 0:
        budget -= price_of_item
        profit += price_of_item * 0.40
        total += price_of_item * 1.4
        print(f"{price_of_item * 1.4:.2f}", end=" ")


if total + budget >= 150:
    print()
    print(f"Profit: {profit:.2f}")
    print("Hello, France!")
else:
    print()
    print(f"Profit: {profit:.2f}")
    print("Not enough money.")
