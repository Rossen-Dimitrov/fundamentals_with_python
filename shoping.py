budget = float(input())
video = int(input())
processors = int(input())
ram = int(input())

video_price = 250
processors_price = (video * video_price) * 0.35
ram_price = (video * video_price) * 0.10

total_sum = video * video_price + processors * processors_price + ram * ram_price


if video > processors:
    total_sum *= 0.85
difference = abs(budget - total_sum)
if budget >= total_sum:

    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")

