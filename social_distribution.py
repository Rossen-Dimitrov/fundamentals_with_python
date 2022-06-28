population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

for num, value in enumerate(population):
    maximum = max(population)
    max_index = population.index(maximum)
    if value < minimum_wealth <= maximum - abs(value - minimum_wealth):
        population[num] = minimum_wealth
        population[max_index] -= abs(value - minimum_wealth)
if sum(population) / len(population) < minimum_wealth:
    print("No equal distribution possible")
else:
    print(population)