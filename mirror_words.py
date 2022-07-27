import re

text = input()
mirror_words = []
pattern = r"(@|#)(?P<word>[A-Za-z]{3,}\1\1[A-Za-z]{3,})\1"
counter = 0
matches = re.finditer(pattern, text)
for match in matches:
    counter += 1
    half = len(match["word"]) // 2
    if match["word"] == match["word"][::-1]:
        mirror_words.append(match["word"][:half - 1] + ' <=> ' + match["word"][half + 1:])

if counter == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{counter} word pairs found!")
    if mirror_words:
        print("The mirror words are:")
        print(", ".join(mirror_words))
    else:
        print("No mirror words!")
