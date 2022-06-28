trip = float(input())
puzzels = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_price = 2.60 * puzzels + 3 * dolls + 4.10 * bears + 8.20 * minions + 2 * trucks
total_order = puzzels + dolls + bears + minions + trucks
if total_order >= 50:
   total_price *= 0.75
total_price *= 0.90

needed_money = abs(trip - total_price)

if total_price >= trip:
    print(f"Yes! {needed_money:.2f} lv left.")
else:
    print(f"Not enough money! {needed_money:.2f} lv needed.")