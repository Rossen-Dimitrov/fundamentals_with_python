from math import pi
figure = input()

if figure == ("square"):
    num1 = float(input())
    result = num1 * num1
    print(f'{result:.3f}')

elif figure == ("rectangle"):
    num1 = float(input())
    num2 = float(input())
    result = num1 * num2
    print(f'{result:.3f}')

elif figure == ("circle"):
    num1 = float(input())
    result = (num1 ** 2) * pi
    print(f'{result:.3f}')

elif figure == ("triangle"):
    num1 = float(input())
    num2 = float(input())
    result = (num1 * num2) / 2
    print(f'{result:.3f}')