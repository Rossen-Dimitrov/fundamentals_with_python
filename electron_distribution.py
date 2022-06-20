number_of_electrons = int(input())
electrons_list = []
n = 1
while number_of_electrons > 0:
    electrons = 2 * (n ** 2)
    if number_of_electrons - electrons < 0:
        electrons_list.append(number_of_electrons)
        break
    electrons_list.append(electrons)
    number_of_electrons -= electrons
    n += 1
print(electrons_list)