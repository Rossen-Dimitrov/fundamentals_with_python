working_hour = int(input())
working_day = input()

if 10 <= working_hour <= 18 and working_day in "Monday Tuesday Wednesday Thursday Friday Saturday":
    print("open")
else:
    print("closed")
