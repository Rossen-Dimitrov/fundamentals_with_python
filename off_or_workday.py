day = input()

if day in 'Saturday Sunday':
    print("Weekend")
elif day in "Monday Tuesday Wednesday Thursday Friday":
    print("Working Day")
else:
    print("Error")
