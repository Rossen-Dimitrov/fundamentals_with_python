divisor = int(input())
boundary = int(input())
for n in range(boundary, divisor, - 1):
    if (0 < n <= boundary) and n % divisor == 0:
        print(n)
        break
#
#
# divisor = int(input())
# boundary = int(input())
# print(boundary//divisor*divisor)