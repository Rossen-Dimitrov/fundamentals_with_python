budget = float(input())
kg_flour = float(input())
milk_one_bread = (kg_flour * 1.25) / 4
pack_of_eggs = kg_flour * 0.75
price_for_bread = pack_of_eggs + kg_flour + milk_one_bread
colored_eggs = 0
easter_breads = 0

while budget >= 0:
    if budget - price_for_bread >= 0:
        budget -= price_for_bread
        easter_breads += 1
        colored_eggs += 3
    else:
        break
    if easter_breads % 3 == 0:
        colored_eggs -= easter_breads - 2

print(f"You made {easter_breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")



