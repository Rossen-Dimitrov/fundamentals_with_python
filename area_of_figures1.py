from math import pi

figure = str(input())
area = 0
if figure == "square":
    side_a = float(input())
    area = side_a * side_a
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == "circle":
    side_a = float(input())
    area = side_a * side_a * pi
elif figure == "triangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b / 2

print(f'{area:.3f}')