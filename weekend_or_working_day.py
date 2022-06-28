working_day = input()

if working_day in "Monday Tuesday Wednesday Thursday Friday":
    print("Working day")
elif working_day in "Saturday Sunday":
    print("Weekend")
else:
    print("Error")
