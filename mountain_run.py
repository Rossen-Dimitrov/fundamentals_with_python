world_rec_sec = float(input())
distance = float(input())
sec_meter = float(input())

delay = distance // 50 * 30
total_time = distance * sec_meter + delay


if world_rec_sec > total_time:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    delay = abs(world_rec_sec - total_time)
    print(f"No! He was {delay:.2f} seconds slower.")

