import math


def center_point(x1, y1, x2, y2):
    if (x2-0)**2 + (y2-0)**2 >= (x1-0)**2 + (y1-0)**2:
        return x1, y1
    else:
        return x2, y2


x_1, y_1, x_2, y_2 = math.floor(float(input())), math.floor(float(input())),\
                     math.floor(float(input())), math.floor(float(input()))
a, b = center_point(x_1, y_1, x_2, y_2)
print(f"({int(a)}, {int(b)})")
