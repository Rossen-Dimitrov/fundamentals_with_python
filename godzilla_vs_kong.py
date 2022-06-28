movie_budget = float(input())
statists = int(input())
price_per_suit = float(input())

decor = movie_budget * 0.1

if statists > 150:
    price_per_suit *= 0.9

total_sum = statists * price_per_suit + decor
difference = abs(movie_budget - total_sum)

if total_sum < difference:
    print(f"Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
