destination = str(input())
dates = str(input())
stays = int(input())
price = 0

if destination == "France":
    if dates == "21-23":
        price = 30
    elif dates == "24-27":
        price = 35
    elif dates == "28-31":
        price = 40
elif destination == "Italy":
    if dates == "21-23":
        price = 28
    elif dates == "24-27":
        price = 32
    elif dates == "28-31":
        price = 39
elif destination == "Germany":
    if dates == "21-23":
        price = 32
    elif dates == "24-27":
        price = 37
    elif dates == "28-31":
        price = 43

total = price * stays
print(f"Easter trip to {destination} : {total:.2f} leva.")