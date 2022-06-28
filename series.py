budget = float(input())
serial_count = int(input())


for count in range(serial_count):
    serial_name = str(input())
    price = float(input())
    if serial_name == "Thrones":
        budget -= price * 0.5
    elif serial_name == "Lucifer":
        budget -= price * 0.6
    elif serial_name == "Protector":
        budget -= price * 0.7
    elif serial_name == "TotalDrama":
        budget -= price * 0.8
    elif serial_name == "Area":
        budget -= price * 0.9
    else:
        budget -= price
if budget >= 0:
    print(f"You bought all the series and left with {budget:.2f} lv.")
else:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")
