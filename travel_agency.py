city = input()
packet_type = input()
vip = input()
stays = int(input())
price = 0

if city in "Bansko Borovets":
    if packet_type == "withEquipment":
        price = 100
        if vip == "yes":
            price *= 0.90
    elif packet_type == "noEquipment":
        price = 80
        if vip == "yes":
            price *= 0.95
    else:
        print("Invalid input!")
        exit()

elif city in "Varna Burgas":
    if packet_type == "withBreakfast":
        price = 130
        if vip == "yes":
            price *= 0.88
    elif packet_type == "noBreakfast":
        price = 100
        if vip == "yes":
            price *= 0.93
    else:
        print("Invalid input!")
        exit()
else:
    print("Invalid input!")
    exit()

if stays < 1:
    print("Days must be positive number!")
    exit()

if stays > 7:
    stays -= 1
price = stays * price
print(f"The price is {price:.2f}lv! Have a nice time!")

