n = int(input())
opening_bracket = False

for i in range(n):
    symbol = input()

    if symbol == "(":
        if opening_bracket:
            break
        else:
            opening_bracket = True

    if symbol == ")":
        if not opening_bracket:
            opening_bracket = True
            break
        else:
            opening_bracket = False

if not opening_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")

