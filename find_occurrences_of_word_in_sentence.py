import re

sentence = input()
searched = input()

pattern = fr"\b{searched}\b"

matches = re.findall(pattern, sentence, flags = re.IGNORECASE)
print(len(matches))
