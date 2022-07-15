line_in = input().split()
repeated = ''
for word in line_in:
    repeated += word * len(word)
print(repeated)