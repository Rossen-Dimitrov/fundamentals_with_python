excursion = float(input())
puzzle = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.6
dolls_price = 3
bears_price = 4.1
minions_price = 8.2
trucks_price = 2

total_number = puzzle + dolls + bears + minions + trucks
total_price = puzzle_price * puzzle + dolls_price * dolls + bears_price * bears + \
minions_price * minions + trucks_price * trucks

if total_number >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.9

money = abs(total_price - excursion)

if total_price >= excursion:
    print(f"Yes! {money:.2f} lv left.")
else:
    print(f"Not enough money! {money:.2f} lv needed.")


