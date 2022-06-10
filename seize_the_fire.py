command_in = input().split('#')
available_water = int(input())
effort = 0
put_out_cells = []

for f_cell in command_in:
    command = f_cell.split(' = ')
    type_of_fire = command[0]
    fire_level = int(command[1])
    if type_of_fire == 'High' and 80 < fire_level <= 125:
        if available_water - fire_level >= 0:
            available_water -= fire_level
            effort += fire_level * 0.25
            put_out_cells.append(fire_level)
    elif type_of_fire == 'Medium' and 50 < fire_level <= 80:
        if available_water - fire_level >= 0:
            available_water -= fire_level
            effort += fire_level * 0.25
            put_out_cells.append(fire_level)
    elif type_of_fire == 'Low' and 0 < fire_level <= 50:
        if available_water - fire_level >= 0:
            available_water -= fire_level
            effort += fire_level * 0.25
            put_out_cells.append(fire_level)

print("Cells:")
for cells in put_out_cells:
    print(f" - {cells}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_cells)}")