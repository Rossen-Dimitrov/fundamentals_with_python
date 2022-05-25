n = int(input())
not_char = [",", ".", "_"]

for _ in range(n):
    strings_input = input()
    if any(char in strings_input for char in not_char):
        print(f"{strings_input} is not pure!")
    else:
        print(f"{strings_input} is pure.")


# n = int(input())
# not_char = [",", ".", "_"]
#
# for _ in range(n):
#     strings_input = input()
#     is_not_pure = False
#     for char in strings_input:
#         if char in not_char:
#             is_not_pure = True
#     if is_not_pure:
#         print(F"{strings_input} is not pure!")
#     else:
#         print(f"{strings_input} is pure.")


