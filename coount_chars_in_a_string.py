from collections import defaultdict

text = input()

letter_dict = defaultdict(int)
for letter in text:
    if not letter == ' ':
        letter_dict[letter] += 1

for letter, count in letter_dict.items():
    print(f"{letter} -> {count}")
