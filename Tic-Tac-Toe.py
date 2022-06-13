def tic_tac_toe(raw_1, raw_2, raw_3):
    if raw_1[0] == raw_1[1] == raw_1[2]:
        return raw_1[0]
    if raw_2[0] == raw_2[1] == raw_2[2]:
        return raw_2[0]
    if raw_3[0] == raw_3[1] == raw_3[2]:
        return raw_3[0]
    if raw_1[0] == raw_2[0] == raw_3[0]:
        return raw_1[0]
    if raw_1[1] == raw_2[1] == raw_3[1]:
        return raw_1[1]
    if raw_1[2] == raw_2[2] == raw_3[2]:
        return raw_1[2]
    if raw_1[0] == raw_2[1] == raw_3[2]:
        return raw_1[0]
    if raw_1[2] == raw_2[1] == raw_3[0]:
        return raw_1[2]


first = input().split()
second = input().split()
third = input().split()

if tic_tac_toe(first, second, third) == "1":
    print("First player won")
elif tic_tac_toe(first, second, third) == "2":
    print("Second player won")
else:
    print("Draw!")


