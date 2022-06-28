city = input()
trade = float(input())
commission = 0
condition = True

if city == "Sofia":
    if 0 < trade <= 500:
        commission = 0.05
    elif 500 < trade <= 1000:
        commission = 0.07
    elif 1000 < trade <= 10000:
        commission = 0.08
    elif trade > 10000:
        commission = 0.12
    else:
        print("error")
        condition = False
elif city == "Varna":
    if 0 < trade <= 500:
        commission = 0.045
    elif 500 < trade <= 1000:
        commission = 0.075
    elif 1000 < trade <= 10000:
        commission = 0.1
    elif trade > 10000:
        commission = 0.13
    else:
        print("error")
        condition = False
elif city == "Plovdiv":
    if 0 < trade <= 500:
        commission = 0.055
    elif 500 < trade <= 1000:
        commission = 0.08
    elif 1000 < trade <= 10000:
        commission = 0.12
    elif trade > 10000:
        commission = 0.145
    else:
        print("error")
        condition = False
else:
    print("error")
    condition = False

if condition:
    print(f"{commission * trade:.2f}")



