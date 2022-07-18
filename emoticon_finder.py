line_in = input().split()
for words in line_in:
    for index in range(len(words)):
        if words[index] == ":":
            print(words[index] + words[index + 1])
            