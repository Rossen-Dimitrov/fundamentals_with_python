min_control = int(input())
sec_control = int(input())
length = float(input())
sec_100 = int(input())

controlla = min_control * 60 + sec_control
delay = (length / 120) * 2.5
time = (length / 100) * sec_100 - delay
difference = time - controlla
if time <= controlla:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")

