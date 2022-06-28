current_sum = float(input())    # Сумата, с която разполагаме - реално число в интервала [10.00…1000.00]
gender = str(input())   # Пол - символ ('m' за мъж и 'f' за жена)
age = int(input())  # Възраст - цяло число в интервала [5…105]
sport = str(input())   # Спорт - текст (една от възможностите в таблицата)
price = 0

if sport == "Gym":
    if gender =="m":
        price = 42
    else:
        price = 35
elif sport == "Boxing":
    if gender == "m":
        price = 41
    else:
        price = 37
elif sport == "Yoga":
    if gender == "m":
        price = 45
    else:
        price = 42
elif sport == "Zumba":
    if gender == "m":
        price = 34
    else:
        price = 31
elif sport == "Dances":
    if gender == "m":
        price = 51
    else:
        price = 53
elif sport == "Pilates":
    if gender == "m":
        price = 39
    else:
        price = 37
if age <= 19:
    price *= 0.8

if  price <= current_sum:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${price - current_sum:.2f} more.")