hours = int(input())
days = int(input())
employees = int(input())

working_hours = days * 0.9 * 8
overtime = employees * 2
total_working = int(working_hours + (overtime * days))

difference = abs(hours - total_working)

if total_working >= hours:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{difference} hours needed.")

