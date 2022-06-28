import math

balls = int(input())
points = 0
red = 0
orange = 0
yellow = 0
white = 0
other = 0
divides = 0
for n in range(balls):
    color = str(input())
    if color == "red":
        points += 5
        red += 1
    elif color == "orange":
        points += 10
        orange += 1
    elif color == "yellow":
        points +=  15
        yellow += 1
    elif color == "white":
        points +=  20
        white += 1
    elif color == "black":
        points /= 2
        divides += 1
        points = math.floor(points)
    else:
        other += 1
print(f"Total points: {points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {divides}")
