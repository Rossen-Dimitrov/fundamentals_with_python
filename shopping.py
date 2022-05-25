budget = int(input())
prices = input()
while not prices == "End":
    budget -= int(prices)
    if budget < 0:
        break
    prices = input()
if budget >= 0:
    print("You bought everything needed.")
else:
    print("You went in overdraft!")
