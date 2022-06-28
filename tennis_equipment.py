import math

t_rocket_price = float(input())       # •	Цена на една тенис ракета – реално число в интервала [0.00…100000.00]
num_t_rockets = int(input())    # •	Брой тенис ракети - цяло число в интервала [0…100]
snickers = int(input())         # •	Брой чифтове маратонки - цяло число в интервала [0…100]
snickers_price = t_rocket_price / 6

total_r_s = t_rocket_price * num_t_rockets + snickers_price * snickers
other_equipment = total_r_s * 0.2
total = total_r_s + other_equipment

print(f"Price to be paid by Djokovic {math.floor(total / 8)}")
print(f"Price to be paid by sponsors {math.ceil((total / 8) * 7)}")

