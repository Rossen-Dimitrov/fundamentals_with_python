number = float(input())

if number <= 10:
    print("SLOW")

elif 10 < number <= 50:
    print("AVERAGE")

elif 50 < number <= 150:
    print("FAST")

elif 150 < number <= 1000:
    print("ULRTA FAST")

else:
    print("EXTREMELY FAST")
