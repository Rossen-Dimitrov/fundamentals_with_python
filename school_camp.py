season = (input())
groupe_type = (input())
students = int(input())
nights = int(input())
sport = ""
price = 0

if season == "Winter":
    if groupe_type == "mixed":
        price = 10
    else:
        price = 9.6
elif season == "Spring":
    if groupe_type == "mixed":
        price = 9.5
    else:
        price = 7.2
elif season == "Summer":
    if groupe_type == "mixed":
        price = 20
    else:
        price = 15
if 10 <= students < 20:
    price *= 0.95
elif 20 <= students < 50:
    price *= 0.85
elif students >= 50:
    price *= 0.5

if season == "Winter":
    if groupe_type == "girls":
        sport = "Gymnastics"
    elif groupe_type == "boys":
        sport = "Judo"
    else:
        sport = "Ski"
elif season == "Spring":
    if groupe_type == "girls":
        sport = "Athletics"
    elif groupe_type == "boys":
        sport = "Tennis"
    else:
        sport = "Cycling"
elif season == "Summer":
    if groupe_type == "girls":
        sport = "Volleyball"
    elif groupe_type == "boys":
        sport = "Football"
    else:
        sport = "Swimming"
total = price * students * nights
print(f"{sport} {total:.2f} lv.")
