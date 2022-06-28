a_1 = int(input())
a_2 = int(input())
n = int(input())
for first in range(a_1, a_2):
    if not first % 2 == 0:
        for second in range(1, n):
            for third in range(1, int(n / 2)):
                if not (second + third + first) % 2 == 0:
                    print(f"{chr(first)}-{second}{third}{first}")
