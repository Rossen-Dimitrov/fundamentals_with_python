deposit = float(input('Депозирана сума: '))
months = int(input('Срок в месеци: '))
annual_interest_percent = float(input('Годишен Лихвен процент: '))

annual_interest = deposit * annual_interest_percent / 100
monthly_interest = annual_interest / 12
total_sum = deposit + (months * monthly_interest)
print(total_sum)