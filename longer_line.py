import math


def longer_line(xy1, xy2, xy3, xy4):
    x = 0
    y = 1
    if (xy2[x]-xy1[x])**2 + (xy2[y]-xy1[y])**2 > (xy4[x]-xy3[x])**2 + (xy4[y]-xy3[y])**2:
        return center_point(xy1, xy2)
    elif (xy2[x]-xy1[x])**2 + (xy2[y]-xy1[y])**2 < (xy4[x]-xy3[x])**2 + (xy4[y]-xy3[y])**2:
        return center_point(xy3, xy4)
    else:
        if center_point(xy1, xy2) < center_point(xy3, xy4):
            return center_point(xy1, xy2)
        else:
            return center_point(xy3, xy4)


def center_point(xy1, xy2):
    x = 0
    y = 1
    if (xy2[x] - 0) ** 2 + (xy2[y] - 0) ** 2 >= (xy1[y] - 0) ** 2 + (xy1[y] - 0) ** 2:
        return xy1, xy2
    else:
        return xy2, xy1


xy_1 = float(input()), float(input())
xy_2 = float(input()), float(input())
xy_3 = float(input()), float(input())
xy_4 = float(input()), float(input())

a, b = longer_line(xy_1, xy_2, xy_3, xy_4)
print(f"({math.floor(a[0])}, {math.floor(a[1])})({math.floor(b[0])}, {math.floor(b[1])})")
