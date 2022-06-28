budget = float(input())
products = 0
total = 0
for n in range(1, 200):
    product_name = str(input())
    if product_name == "Stop" or budget == 0:
        print(f"You bought {products} products for {total:.2f} leva.")
        break
    price = float(input())
    if n % 3 == 0:
        price /= 2
        total += price
        products += 1
    else:
        total += price
        products += 1
    if total > budget:
        print("You don't have enough money!")
        print(f"You need {(total - budget):.2f} leva!")
        break