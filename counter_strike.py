energy = int(input())
distance = input()
count = 0
out_of_energy = False
while not distance == "End of battle":
    distance = int(distance)
    if energy - distance >= 0:
        energy -= distance
        count += 1
        if count % 3 == 0:
            energy += count
    else:
        out_of_energy = True
        break
    distance = input()
if out_of_energy:
    print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
else:
    print(f"Won battles: {count}. Energy left: {energy}")
