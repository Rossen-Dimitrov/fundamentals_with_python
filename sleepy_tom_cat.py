off_days = int(input())

playing_time = (365 - off_days) * 63 + (off_days * 127)

difference = abs(30000 - playing_time)
hours = difference // 60
minutes = difference % 60

if playing_time > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
