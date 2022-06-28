amount = float(input())
period = int(input())
interest = float(input()) / 100
interest_per_month = (amount * interest) / 12
total = amount + (period * interest_per_month)
print(total)

