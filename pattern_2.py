number = int(input())

for i in range(number):
    print("  " * i + "* " * (number - i))
for i in range(2, number + 1):
    print("  " * (number - i) + "* " * i)

