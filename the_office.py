happiness = list(map(int, input().split()))
factor = int(input())
# multiply_happiness = [x * factor for x in happiness]
sum_of_happiness = sum(happiness)
average = sum_of_happiness / len(happiness)
counter = 0
for employ in happiness:
    if employ >= average:
        counter += 1
if counter >= len(happiness) / 2:
    print(f"Score: {counter}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(happiness)}. Employees are not happy!")
