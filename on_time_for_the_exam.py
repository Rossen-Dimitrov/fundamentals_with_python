exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

total_exam = (exam_hour * 60) + exam_min
total_arrive = (arrive_hour * 60) + arrive_min

diff = abs(total_exam - total_arrive)
hours = diff // 60
minutes = diff % 60

if total_arrive > total_exam:
    print("Late")
    if diff >= 60:
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{minutes} minutes after the start")

if (total_arrive <= total_exam) and diff <= 30:
    if diff == 0:
        print("On time")
    else:
        print("On time")
        print(f"{minutes} minutes before the start")

if total_arrive < total_exam and diff > 30:
    print("Early")
    if diff >= 60:
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{minutes} minutes before the start")
