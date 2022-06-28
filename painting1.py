naylon = int(input())
paint = int(input())
diluent = int(input())
working_hours = int(input())

nylon_price = 1.5
paint_price = 14.5
diluent_price = 5
total_sum_mterials = (paint * 1.1 * paint_price) + (naylon + 2) * nylon_price + (diluent * diluent_price) + 0.4
total_sum = total_sum_mterials + (total_sum_mterials * working_hours * 0.3)
print(total_sum)