n = int(input())
salary = float(input())
condition = False
for tabs in range(n):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50
    if salary <= 0:
        condition = True
        break
if not condition:
    print(int(salary))
else:
    print("You have lost your salary.")
