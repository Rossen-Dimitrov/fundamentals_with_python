def is_wined():
    if items["Shadowmourne"] <= 0 or items['Valanyr'] <= 0 or items['Dragonwrath'] <= 0:
        return True


items = {'Shadowmourne': 250, 'Valanyr': 250, 'Dragonwrath': 250}

collected_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}


while True:
    farmed_materials = input().split()
    for i in range(0, len(farmed_materials), 2):
        quantity = int(farmed_materials[i])
        material = str(farmed_materials[i + 1].lower())
        if material == 'shards':
            items["Shadowmourne"] -= quantity
            collected_materials["shards"] += quantity
            if is_wined():
                break
        elif material == 'fragments':
            items["Valanyr"] -= quantity
            collected_materials["fragments"] += quantity
            if is_wined():
                break
        elif material == 'motes':
            items["Dragonwrath"] -= quantity
            collected_materials["motes"] += quantity
            if is_wined():
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity
    if is_wined():
        break


for key, value in items.items():
    if value <= 0:
        print(f'{key} obtained!')

for key, value in collected_materials.items():
    if value >= 250:
        print(f'{key}: {value - 250}')
    else:
        print(f'{key}: {value}')

for key, value in junk.items():
    print(f'{key}: {value}')
