def palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False


numbers = input().split(', ')
for x in numbers:
    print(palindrome(x))

