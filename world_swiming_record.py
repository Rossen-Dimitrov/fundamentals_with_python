old_world_record = float(input())
distance = float(input())
time_per_meter = float(input())

delay = distance // 15 * 12.5
total_time = distance * time_per_meter + delay


if old_world_record > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    differnce = abs(old_world_record - total_time)
    print(f"No, he failed! He was {differnce:.2f} seconds slower.")

