people_in_circle = input().split()
k = int(input())
kill_circle = []
counter = 0
index = 0

while len(people_in_circle) > 0:
    counter += 1
    if counter % k == 0:
        kill_circle.append(people_in_circle.pop(index))
    else:
        index += 1
    if index >= len(people_in_circle):
        index = 0
print(f"[{','.join(kill_circle)}]")
