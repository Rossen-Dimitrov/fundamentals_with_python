time_1 = int(input())
time_2 = int(input())
time_3 = int(input())

total_time = time_1 + time_2 + time_3
minutes = total_time // 60
seconds = int(total_time % 60)

if seconds <= 9:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
