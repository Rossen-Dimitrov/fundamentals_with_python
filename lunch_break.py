from math import ceil

serial_name = str(input())
serial_duration = int(input())
launch_duration = int(input())

launch_time = launch_duration / 8
relax_time = launch_duration / 4

total_time = launch_time + serial_duration + relax_time
left_time = abs(launch_duration - total_time)

if total_time <= launch_duration:
    print(f"You have enough time to watch {serial_name} and left with {ceil(left_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(left_time)} more minutes.")

