fruit = str(input())
size = str(input())
amount = int(input())
price = 0

if fruit == "Watermelon":
    if size == "small":
        price = 56 * 2
    else:
        price = 28.70 * 5
elif fruit == "Mango":
    if size == "small":
        price = 36.66 * 2
    else:
        price = 19.6 * 5
elif fruit == "Pineapple":
    if size == "small":
        price = 42.1 * 2
    else:
        price = 24.80 * 5
elif fruit == "Raspberry":
    if size == "small":
        price = 20 * 2
    else:
        price = 15.20 * 5

total = price * amount

if 400 <= total <= 1000:
    total *= 0.85
elif total > 1000:
    total *= 0.5

print(f"{total:.2f} lv.")
