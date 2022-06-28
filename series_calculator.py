import math

name = str(input())
seasons_count = int(input())
series_count = int(input())
duration = float(input())
commercials = duration * 1.2
total_time = seasons_count * series_count * commercials + (seasons_count * 10)
print(f"Total time needed to watch the {name} series is {math.floor(total_time)} minutes.")