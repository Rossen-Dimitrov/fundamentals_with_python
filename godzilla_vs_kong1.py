budget = float(input())
statists = int(input())
dres_for_statists = float(input())

deckors = budget * 0.1

if statists > 150:
    dres_for_statists *= 0.9

total = statists * dres_for_statists + deckors
difference = abs(budget - total)

if budget - total >= 0:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
