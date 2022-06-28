hour_in = int(input())
minute_in = int(input())

total_time = hour_in * 60 + minute_in + 15
hours = total_time // 60
minutes = total_time % 60
if hours > 23:
    hours = 0
print(f"{hours}:{minutes:02d}")
