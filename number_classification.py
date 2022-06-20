numbers = list(map(int, input().split(', ')))

print(f"Positive: {', '.join(str(x) for x in numbers if x >= 0)}")
print(f"Negative: {', '.join(str(x) for x in numbers if x < 0)}")
print(f"Even: {', '.join(str(x) for x in numbers if x % 2 == 0)}")
print(f"Odd: {', '.join(str(x) for x in numbers if not x % 2 == 0)}")
