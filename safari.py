budget = float(input())    # •	Бюджет – реално число в интервала [0.00… 10000.00]
fuel = int(input())    # •	Колко литра гориво ще са им нужни – реално число в интервала [1.00… 50.00]
day = str(input())    # •	Ден от седмицата – текст с възможности "Saturday" и "Sunday"

price_fuel = 2.10
guide = 100

total = guide + fuel * price_fuel

if day == "Saturday":
    total *= 0.9
else:
    total *= 0.8

difference = abs(total - budget)
if budget >= total:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
