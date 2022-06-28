man_count = int(input())
women_count = int(input())
tables = int(input())
counter = 0
for man in range(1, man_count +1):
    for woman in range(1, women_count + 1):
        if counter < tables:
            counter += 1
            print(f'({man} <-> {woman})', end=" ")
