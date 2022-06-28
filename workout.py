import math

n_days = int(input())
m_km = float(input())
current_run = m_km
total = m_km
for n in range(1, n_days + 1):
    percent_increase = int(input())
    current_run = current_run + (current_run * percent_increase / 100)
    total += current_run
if total <= 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(1000 - total)} more kilometers")
else:
    print(f"You've done a great job running {math.ceil(total - 1000)} more kilometers!")