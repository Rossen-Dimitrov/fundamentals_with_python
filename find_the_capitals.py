str_input = input()
indexes = []
for index, char in enumerate(str_input):
    if char.isupper():
        indexes.append(index)
print(indexes)
