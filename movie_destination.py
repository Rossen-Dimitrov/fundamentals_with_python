budget = float(input())         # 1.	Бюджет на филма – реално число в диапазона [100 000.0… 2 000 000.0]
destination = str(input())      # 2.	Дестинация – текст, с възможности "Dubai", "Sofia" и "London"
season = str(input())           # 3.	Сезон – текст, с възможности "Summer" и "Winter"
days = int(input())             # 4.	Брой дни  – цяло число в диапазона [1… 40]
price = 0

if destination == "Dubai":
    if season == "Winter":
        price = 0.7 * 45000
    else:
        price = 0.7 * 40000
elif destination == "Sofia":
    if season == "Winter":
        price = 1.25 * 17000
    else:
        price = 1.25 * 12500
else:
    if season == "Winter":
        price = 24000
    else:
        price = 20250

total = price * days
difference = abs(budget - total)
if budget >= total:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
