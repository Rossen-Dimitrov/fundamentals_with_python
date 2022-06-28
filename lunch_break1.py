import math
serial_name = str(input())
serial_duration = int(input())
break_duration = int(input())

launc_time = break_duration / 8
relax_time = break_duration / 4

time_left = break_duration - launc_time - relax_time
difference = math.ceil(abs(time_left - serial_duration))

if time_left >= serial_duration:
    print(f"You have enough time to watch {serial_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {difference} more minutes.")