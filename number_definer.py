number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if number < 1:
        print("small", end=" ")
    elif number > 1000000:
        print("large", end=" ")
    print("positive")
elif number < 0:
    if number > -1:
        print("small", end=" ")
    elif number < -100000:
        print("large", end=" ")
    print("negative")
