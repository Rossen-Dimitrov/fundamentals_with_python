juniors = int(input())
seniors = int(input())
trase = str(input())

taxes_juniors = 0
taxes_seniors = 0

if trase == "trail":
    taxes_juniors = 5.5
    taxes_seniors = 7
elif trase == "cross-country":
    taxes_juniors = 8
    taxes_seniors = 9.5
    if seniors + juniors >= 50:
        taxes_juniors *= 0.75
        taxes_seniors *= 0.75
elif trase == "downhill":
    taxes_juniors = 12.25
    taxes_seniors = 13.75
elif trase == "road":
    taxes_juniors = 20
    taxes_seniors = 21.5


total = (taxes_juniors * juniors + taxes_seniors * seniors) * 0.95
print(f"{total:.2f}")