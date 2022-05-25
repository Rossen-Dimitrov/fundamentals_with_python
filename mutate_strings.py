first_word = str(input())
second_word = str(input())
new_word = []
if first_word == second_word:
    exit()
else:
    for index in range(len(first_word)):
        temp_word = second_word[:index + 1] + first_word[index + 1:]
        if temp_word not in new_word:
            new_word.append(temp_word)
            print(temp_word)


# print(new_word)
#
# first_word = str(input())
# second_word = str(input())
# new_word = first_word
#
# for index in range(len(first_word)):
#     temp_word = second_word[:index + 1] + first_word[index + 1:]
#     if not temp_word == new_word:
#         new_word = temp_word
#         print(temp_word)