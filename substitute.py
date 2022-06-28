k = int(input())
l = int(input())
m = int(input())
n = int(input())
counter = 0

for kk in range(k, 8 + 1):
    for ll in range(9, l - 1, - 1):
        for mm in range(m, 8 + 1):
            for nn in range(9, n - 1, - 1):
                if counter < 6:
                    if kk % 2 == 0 and ll % 2 != 0 and mm % 2 == 0 and nn % 2 != 0:
                        if kk == mm and ll == nn:
                            print("Cannot change the same player.")
                        else:
                            counter += 1
                            print(f"{kk}{ll} - {mm}{nn}")



