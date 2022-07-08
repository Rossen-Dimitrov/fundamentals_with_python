data_in = input().split()
odd_word = {}
for word in data_in:
    word = word.lower()
    if word not in odd_word:
        odd_word[word] = 0
    odd_word[word] += 1

for word, value in odd_word.items():
    if not value == 2:
        print(word, end=' ')
