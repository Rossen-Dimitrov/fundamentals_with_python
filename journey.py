budget = float(input())
season = input()
destination = ""
type_of_vacation = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.3
        type_of_vacation = "Camp"
    elif season == "winter":
        budget *= 0.7
        type_of_vacation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    type_of_vacation = "Hotel"
    if season == "summer":
        budget *= 0.4
        type_of_vacation = "Camp"
    elif season == "winter":
        budget *= 0.8
        type_of_vacation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    type_of_vacation = "Hotel"
    budget *= 0.9

print(f"Somewhere in {destination}" )
print(f"{type_of_vacation} - {budget:.2f}")
