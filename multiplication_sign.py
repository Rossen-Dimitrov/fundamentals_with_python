def multiplication(x, y ,z):
    if x * y * z > 0:
        print('positive')
    elif x * y * z < 0:
        print('negative')
    else:
        print("zero")


int1, int2, int3 = int(input()), int(input()), int(input())
multiplication(int1, int2, int3)