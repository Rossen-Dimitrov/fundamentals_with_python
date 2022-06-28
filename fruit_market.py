strawberry_price = float(input())
banana_kg = float(input())
orange_kg = float(input())
raspberry_kg = float(input())
strawberry_kg = float(input())
raspberry_price = strawberry_price / 2
orange_price = 0.6 * raspberry_price
banana_price = 0.2 * raspberry_price

total = strawberry_kg * strawberry_price + banana_price * banana_kg + orange_price * orange_kg\
        + raspberry_kg * raspberry_price
print(f"{total:.2f}")