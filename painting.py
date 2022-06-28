nylon = int(input('найлон = '))
paint = int(input('боя = '))
diluent = int(input('разредител = '))
working_hours = int(input('часове = '))
nylon_prise = 1.5 * (nylon + 2)
paint_prise = 14.5 * (paint * 1.10)
diluent_prise = 5 * diluent
bag = 0.4
sum = nylon_prise + paint_prise + diluent_prise + bag
total_sum = (sum * 0.30) * working_hours + sum
print(total_sum)

