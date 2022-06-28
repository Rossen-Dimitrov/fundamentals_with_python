import math
current_wr = float(input())
distance_m = float(input())
time_for_meter = float(input())

delay = math.floor(distance_m // 15) * 12.5

swimmer_time = time_for_meter * distance_m + delay

if swimmer_time < current_wr:
    print(f" Yes, he succeeded! The new world record is {swimmer_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {swimmer_time - current_wr:.2f} seconds slower.")
