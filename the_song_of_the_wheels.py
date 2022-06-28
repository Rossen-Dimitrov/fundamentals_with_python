user_input = int(input())
counter = 0
password = 0
condition = False
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == user_input:
                    if a < b and c > d:
                        counter += 1
                        print(f"{a}{b}{c}{d}", end=" ")
                        if counter == 4:
                            password = str(a) + str(b) + str(c) + str(d)
                            condition = True
if condition:
    print()
    print(f"Password: {password}")
else:
    print()
    print("No!")

