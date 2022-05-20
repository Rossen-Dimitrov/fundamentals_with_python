for _ in range(int(input())):
    num = int(input())

    if not num % 2 == 0:
        print(f"{num} is odd!")
        break
else:
    print(f"All numbers are even.")
