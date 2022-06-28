x = float(input()) #– височината на къщата – реално число в интервала [2...100]
y = float(input()) #– дължината на страничната стена – реално число в интервала [2...100]
h = float(input()) #– височината на триъгълната стена на прокрива – реално число в интервала [2...100]

front_wals = (x * x * 2) - (1.2 * 2)
side_wals = (x * y * 2) - (1.5 * 1.5 * 2)
roof_side =  x * y * 2
roof_triangle = (x * h)
green_paint = (front_wals + side_wals) / 3.4
red_paint = (roof_side + roof_triangle) / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
# Разхода на зелената боя е 1 литър за 3.4 м2, а на червената – 1 литър за 4.3 м2.