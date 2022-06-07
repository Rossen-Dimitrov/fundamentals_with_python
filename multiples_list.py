factor = int(input())
count = int(input())
multiples = []
for num in range(factor, count * factor + 1, factor):
    multiples.append(num)
print(multiples)
