budget = float(input())
statists = int(input())
dress_price = float(input())

deckor_price = budget * 0.1

if statists > 150:
    dress_price *= 0.9

total_price = statists * dress_price + deckor_price
difference = abs(budget - total_price)

if budget >= total_price:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")


