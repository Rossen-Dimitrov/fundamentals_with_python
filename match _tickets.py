budget = float(input())
cateogry = input()
people = int(input())
transport = 0

if cateogry == "VIP":
    price = 499.99
else:
    price = 249.99
if people <= 4:
    transport = budget * 0.75
elif people <= 9:
    transport = budget * 0.60
elif people <= 24:
    transport = budget * 0.50
elif people <= 49:
    transport = budget * 0.40
elif people > 49:
    transport = budget * 0.25
total = transport + price * people
diff = abs(budget - total)
if total <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")