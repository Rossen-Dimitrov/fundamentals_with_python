till_20_kg = float(input())
kg_bags = float(input())
days_to_trip = int(input())
bag_count = int(input())

if kg_bags < 10:
    till_20_kg *= 0.2
elif kg_bags <= 20:
    till_20_kg *= 0.5

if days_to_trip < 7:
    till_20_kg *= 1.4
elif days_to_trip <= 30:
    till_20_kg *= 1.15
else:
    till_20_kg *= 1.1

total = till_20_kg * bag_count

print(f" The total price of bags is: {total:.2f} lv. ")
