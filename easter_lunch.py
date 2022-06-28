easter_bread = int(input())
egs_kori = int(input())
cookies = int(input())
easter_bread_price = 3.2
egs_cena_kora = 4.35
cookies_price_kg = 5.4
paint_egg = 0.15

total = easter_bread * easter_bread_price + egs_kori * egs_cena_kora\
        + cookies * cookies_price_kg + (egs_kori * 12 * paint_egg)
print(f"{total:.2f}")