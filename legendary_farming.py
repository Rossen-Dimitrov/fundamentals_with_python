def is_wined(x):
    if collected_materials[x] >= 250:
        return True


collected_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
condition = False

while True:
    farmed_materials = input().split()
    for i in range(0, len(farmed_materials), 2):
        quantity = int(farmed_materials[i])
        material = str(farmed_materials[i + 1].lower())
        if material in collected_materials:
            collected_materials[material] += quantity
            if is_wined(material):
                condition = True
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity
    if condition:
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

for key, value in junk.items():
    print(f'{key}: {value}')
