screening_type = input()
rows = int(input())
columns = int(input())
income = 0
total_places = rows * columns

if screening_type == "Premiere":
    income = total_places * 12
elif screening_type == "Normal":
    income = total_places * 7.5
elif screening_type == "Discount":
    income = total_places * 5
print(f"{income:.2f}")