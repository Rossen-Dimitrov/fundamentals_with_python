chrysanthemum = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
chrysanthemum_price = 0
rose_price = 0
tulip_price = 0

if season in "Spring, Summer":
    chrysanthemum_price = 2
    rose_price = 4.1
    tulip_price = 2.5
elif season in "Autumn, Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.5
    tulip_price = 4.15

total = chrysanthemum * chrysanthemum_price + roses * rose_price + tulips * tulip_price

if holiday == "Y":
    total *= 1.15

if tulips > 7 and season == "Spring":
    total *= 0.95
if roses >= 10 and season == "Winter":
    total *= 0.9
if (roses + tulips + chrysanthemum) > 20:
    total *= 0.8
print(f"{total + 2:.2f}")
