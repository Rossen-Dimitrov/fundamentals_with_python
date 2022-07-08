n_words = int(input())
word_dict = {}
for _ in range(n_words):
    word = str(input())
    synonym = str(input())
    if word not in word_dict:
        word_dict[word] = []
    word_dict[word] += [synonym]
    # word_dict[word].append(synonym)

for word, synonym in word_dict.items():
    print(f"{word} - {', '.join(synonym)}")

# for word in word_dict
#     print(f"{word} - {', '.join(word_dict[word])}")
