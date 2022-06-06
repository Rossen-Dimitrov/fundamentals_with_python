from math import floor
companion = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    coins += 50
    if day % 10 == 0:
        companion -= 2
    if day % 15 == 0:
        companion += 5
    coins -= 2 * companion
    if day % 3 == 0:
        coins -= 3 * companion
    if day % 5 == 0:
        coins += 20 * companion
        if day % 3 == 0:
            coins -= 2 * companion

print(f"{companion} companions received {floor(coins / companion)} coins each.")