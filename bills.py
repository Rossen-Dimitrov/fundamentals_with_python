months = int(input())
water = 20 * months
internet = 15 * months
electricity = 0
for _ in range(months):
    electricity += float(input())
others = (electricity + water + internet) * 1.2
total = water + internet + others + electricity
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet :.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {total / months:.2f} lv")

