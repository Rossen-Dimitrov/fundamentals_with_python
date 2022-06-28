flours = input()
quantity = int(input())
budget = int(input())
price = 0

if flours == "Roses":
    price = 5
    if quantity > 80:
        price *= 0.9
elif flours == "Dahlias":
    price = 3.8
    if quantity > 90:
        price *= 0.85
elif flours == "Tulips":
    price = 2.8
    if quantity > 80:
        price *= 0.85
elif flours == "Narcissus":
    price = 3
    if quantity < 120:
        price *= 1.15
elif flours == "Gladiolus":
    price = 2.5
    if quantity < 80:
        price *= 1.2

total = price * quantity
difference = abs(budget - total)

if budget >= total:
    print(f"Hey, you have a great garden with {quantity} {flours} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")