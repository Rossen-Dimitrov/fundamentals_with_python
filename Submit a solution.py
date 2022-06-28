total_no_tax = 0
while True:
    command = input()
    if command in ("special", "regular"):
        break
    if float(command) < 0:
        print("Invalid price!")
        continue
    total_no_tax += float(command)
taxes = total_no_tax * 0.2
total = total_no_tax + taxes

if command == "special":
    total *= 0.9
if total_no_tax == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_no_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total:.2f}$")

