import sys

smallest = sys.maxsize
biggest = -sys.maxsize
user_input = int(input())
for cipher in range(0, user_input):
    num = int(input())
    if num < smallest:
        smallest = num
    if num > biggest:
        biggest = num
print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
