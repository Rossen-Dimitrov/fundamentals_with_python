city = input()
sales = float(input())
commission = 0
condition = True

if city == "Sofia":
    if  0 <= sales <= 500:
        commission = 0.05 * sales
    elif 500 < sales <= 1000:
        commission = 0.07 * sales
    elif 1000 < sales <= 10000:
        commission = 0.08 * sales
    elif sales > 10000:
        commission = 0.12 * sales
    else:
        condition = False

elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045 * sales
    elif 500 < sales <= 1000:
        commission = 0.075 * sales
    elif 1000 < sales <= 10000:
        commission = 0.10 * sales
    elif sales > 10000:
        commission = 0.13 * sales
    else:
        condition = False

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055 * sales
    elif 500 < sales <= 1000:
        commission = 0.08 * sales
    elif 1000 < sales <= 10000:
        commission = 0.12 * sales
    elif sales > 10000:
        commission = 0.145 * sales
    else:
        condition = False
else:
    condition = False

if condition:
    print(f'{commission:.2f}')
else:
    print("error")
