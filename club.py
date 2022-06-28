desired_profit = float(input())
cocktail_price = 0
total = 0
for n in range(5000):
    cocktail_name = str(input())
    if cocktail_name == ("Party!"):
        print(f"We need {(desired_profit - total):.2f} leva more.")
        print(f"Club income - {total:.2f} leva.")
        break
    quantity = int(input())
    cocktail_price = len(cocktail_name) * quantity
    if cocktail_price % 2 != 0:
        cocktail_price *= 0.75
        total += cocktail_price
    else:
        total += cocktail_price
    if total >= desired_profit:
        print(f"Target acquired.")
        print(f"Club income - {abs(total):.2f} leva.")
        break

