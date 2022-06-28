distance = int(input())
part_of_day = str(input())
price = 0

if distance < 20:
    if part_of_day == "night":
        price = 0.90
        print(f"{price * distance +0.7:.2f}")
    else:
        price = 0.79
        print(f"{price * distance + 0.7:.2f}")
elif 20 <= distance < 100:
    price = 0.09
    print(f"{price * distance:.2f}")
elif distance >= 100:
    price = 0.06
    print(f"{price * distance:.2f}")

