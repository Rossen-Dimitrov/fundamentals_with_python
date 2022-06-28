def tribonacci(num):
    num1 = 1
    num2 = 0
    num3 = 0
    print("1", end=' ')
    for n in range(1, num):
        result = num1 + num2 + num3
        print(result, end=" ")
        if num2 == 0:
            num2 = result
        elif num3 == 0:
            num3 = result
        else:
            num1 = num2
            num2 = num3
            num3 = result


number = int(input())
tribonacci(number)