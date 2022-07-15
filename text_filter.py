banned = input().split(", ")
text = str(input())

for word in banned:
    while word in text:
        text = text.replace(word, "*" * len(word))

print(text)
