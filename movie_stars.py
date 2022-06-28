budget = float(input())
salary = 0
for n in range(200):
    actor_name = str(input())
    if actor_name == "ACTION" or budget == 0:
        print(f"We are left with {budget:.2f} leva.")
        break
    if len(actor_name) > 15:
        salary = (budget / 100) * 20
        budget -= salary
    else:
        salary = float(input())
        budget -= salary
    if budget < 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break
