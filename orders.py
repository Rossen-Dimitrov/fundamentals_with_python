num_orders = int(input())
total = 0
for n in range(num_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if (0.01 <= price_per_capsule <= 100) and (0 < days <= 31) and (1 <= capsule_per_day <= 2000):
        price = capsule_per_day * price_per_capsule * days
        print(f"The price for the coffee is: ${price:.2f}")
        total += price
print(f"Total: ${total:.2f}")
