version = list(map(int, input().split('.')))
version[2] += 1

for n in range(len(version) - 1, -1, -1):
    if version[n] == 10:
        version[n] = 0
        version[n - 1] += 1
version = list(map(str, version))
print('.'.join(version))
