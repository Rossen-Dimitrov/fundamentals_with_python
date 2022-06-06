n = int(input())
word_list = []
filter_word = str(input())

for _ in range(n):
    word_list.append(input())
print(word_list)
filter_list = list(x for x in word_list if filter_word in x )

print(filter_list)
