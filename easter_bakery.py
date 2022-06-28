flour = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_kori = int(input())
yeast_packs = int(input())

sugar_price = 0.75 * flour
eggs_price = 1.1 * flour
yeast_price = 0.2 * sugar_price

total = flour * flour_kg + sugar_kg * sugar_price + eggs_kori * eggs_price + yeast_price * yeast_packs
print(f"{total:.2f}")
