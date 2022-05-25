quantity = int(input())
days_left = int(input())
total_spirit = 0
budget = 0
decoration_types = {'ornament': [2, 5], 'skirt': [5, 3], 'garland': [3, 10], 'lights': [15, 17]}

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += decoration_types.get("ornament")[0] * quantity
        total_spirit += decoration_types.get("ornament")[1]
    if day % 3 == 0:
        budget += decoration_types.get("skirt")[0] * quantity
        budget += decoration_types.get("garland")[0] * quantity
        total_spirit += decoration_types.get("skirt")[1]
        total_spirit += decoration_types.get("garland")[1]
    if day % 5 == 0:
        budget += decoration_types.get("lights")[0] * quantity
        total_spirit += decoration_types.get("lights")[1]
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        budget += decoration_types.get("lights")[0]
        budget += decoration_types.get("garland")[0]
        budget += decoration_types.get("skirt")[0]
        total_spirit -= 20
if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
