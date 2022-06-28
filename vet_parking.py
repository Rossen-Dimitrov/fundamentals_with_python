days = int(input())
hours_per_day = int(input())
total = 0
for d in range(1, days + 1):
    price_per_day = 0
    for h in range(1, hours_per_day + 1):
        if d % 2 == 0 and not h % 2 == 0:
            price = 2.5
        elif not d % 2 == 0 and h % 2 == 0:
            price = 1.25
        else:
            price = 1
        price_per_day += price
    total += price_per_day
    print(f"Day: {d} - {price_per_day:.2f} leva")
print(f"Total: {total:.2f} leva")