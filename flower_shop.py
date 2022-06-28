import math

magnolia = int(input())
zumbul = int(input())
rose = int(input())
cactus = int(input())
price = float(input())

magnolia_price = 3.25
zumbul_price = 4
rose_price = 3.50
cactus_price = 8
total = (magnolia * magnolia_price + zumbul * zumbul_price + rose_price * rose + cactus_price * cactus)
taxes = total * 0.05
total -= (taxes)
diff = abs(total - price)

if total >= price:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")