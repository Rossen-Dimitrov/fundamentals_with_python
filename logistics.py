all_cargo = int(input())
bus = 0
truck = 0
train = 0
total_weight = 0
average_price = 0
for _ in range(all_cargo):
    weight = int(input())
    total_weight += weight
    if weight <= 3:
        average_price += weight * 200
        bus += weight
    elif weight <= 11:
        average_price += weight * 175
        truck += weight
    else:
        average_price += weight * 120
        train += weight
average_price /= total_weight
print(f"{average_price:.2f}")
print(f"{(bus / total_weight) * 100:.2f}%")
print(f"{(truck / total_weight) * 100:.2f}%")
print(f"{(train / total_weight) * 100:.2f}%")


