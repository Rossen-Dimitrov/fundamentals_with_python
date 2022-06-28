budget = float(input())
season = input()
price = 0
type_class = ""
type_of_car = ""
if budget <= 100:
    type_class = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        type_of_car = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    type_class = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        type_of_car = "Jeep"
        price = budget * 0.80
elif budget > 500:
    type_class = "Luxury class"
    type_of_car = "Jeep"
    price = budget * 0.90

print(type_class)
print(f"{type_of_car} - {price:.2f}")

