n = int(input())
washing_machine = float(input())
toy_price = int(input())
money = 0
toys = 0
for n in range(1, n + 1):
    if n % 2 == 0:
        money += n * 5 - 1
    else:
        toys += 1
total = (toys * toy_price + money)
diff = abs(washing_machine - total)
if total >= washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")