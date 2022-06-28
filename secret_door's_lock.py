hundreds = int(input())
tens = int(input())
units = int(input())

for x100 in range(1, hundreds + 1):
    if x100 % 2 == 0:
        for x10 in range(1, tens + 1):
            if x10 == 2 or x10 == 3 or x10 == 5 or x10 == 7:
                for x1 in range(1, units + 1):
                    if x1 % 2 == 0:
                        print(f"{x100} {x10} {x1}")