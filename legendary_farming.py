def is_wined():
    if collected_materials["shards"] >= 250 or collected_materials["fragments"] >= 250\
            or collected_materials["motes"] >= 250:
        return True


collected_materials = {"shards": 0, "fragments": 0, "motes": 0}

while True:
    farmed_materials = input().split()
    for i in range(0, len(farmed_materials), 2):
        quantity = int(farmed_materials[i])
        material = str(farmed_materials[i + 1].lower())
        if material not in collected_materials:
            collected_materials[material] = 0
        collected_materials[material] += quantity
        if is_wined():
            break
    if is_wined():
        break

for key, value in collected_materials.items():
    if value >= 250:
        if key == "shards":
            collected_materials[key] -= 250
            print('Shadowmourne obtained!')
        if key == "fragments":
            collected_materials[key] -= 250
            print('Valanyr obtained!')
        if key == "motes":
            collected_materials[key] -= 250
            print('Dragonwrath obtained!')

for key, value in collected_materials.items():
    print(f'{key}: {value}')
