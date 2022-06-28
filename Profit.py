leva_1 = int(input())
leva_2 = int(input())
leva_5 = int(input())
amount = int(input())

for lv_1 in range(leva_1 + 1):
    for lv_2 in range(leva_2 + 1):
        for lv_5 in range(leva_5 + 1):
            if lv_1 * 1 + lv_2 * 2 + lv_5 * 5 == amount:
                print(f"{lv_1} * 1 lv. + {lv_2} * 2 lv. + {lv_5} * 5 lv. = {amount} lv.")
