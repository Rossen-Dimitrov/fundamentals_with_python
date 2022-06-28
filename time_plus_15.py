hour = int(input())
min = int(input())
hour *= 60
min += 15
new_time = hour + min
new_min = new_time % 60
new_hour = new_time // 60
if new_hour == 24:
    new_hour = 0
if new_min <10:
    print(f"{new_hour}:0{new_min}")
else:
    print(f"{new_hour}:{new_min}")