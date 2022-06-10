def fire_type(fire, level):
    if fire == 'High' and 80 < level <= 125:
        return True
    elif fire == 'Medium' and 50 < level <= 80:
        return True
    elif fire == 'Low' and 0 < level <= 50:
        return True


command_in = input().split('#')
available_water = int(input())
effort = 0
put_out_cells = []

for f_cell in command_in:
    command = f_cell.split(' = ')
    type_of_fire = command[0]
    fire_level = int(command[1])
    if fire_type(type_of_fire, fire_level) and available_water - fire_level >= 0:
        available_water -= fire_level
        effort += fire_level * 0.25
        put_out_cells.append(fire_level)

print("Cells:")
for cells in put_out_cells:
    print(f" - {cells}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_cells)}")