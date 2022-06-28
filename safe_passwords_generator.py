first = int(input())
second = int(input())
max_passwords = int(input())
counter = 0
for A in range(35, 55):
    for B in range(64, 96):
        for x in range(1, first + 1):
            for y in range(1, second + 1):
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end='|')
                counter += 1
                A += 1
                B += 1
                if A > 55:
                    A = 35
                if B > 96:
                    B = 64
                if first == x and second == y:
                    exit()
                if counter == max_passwords:
                    exit()