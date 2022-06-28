n = int(input())
negatives = list()
positives = list()
for i in range(n):
    command = int(input())
    if command >= 0:
        positives.append(command)
    else:
        negatives.append(command)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")
