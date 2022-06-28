budget = float(input())
nights = int(input())
price = float(input())
additional_costs = int(input())

if nights > 7:
    price *= 0.95

total = nights * price + ((budget / 100) * additional_costs)
diff = abs(budget - total)

if budget >= total:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
