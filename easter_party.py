guests = int(input())
couvert = float(input())
budget = float(input())

cake = budget * 0.10
if guests < 10:
    couvert
elif 10 <= guests <=15:
    couvert *= 0.85
elif guests <= 20:
    couvert *= 0.8
elif guests > 20:
    couvert *= 0.75

total = couvert * guests + cake
difference = abs(budget - total)

if budget >= total:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")
