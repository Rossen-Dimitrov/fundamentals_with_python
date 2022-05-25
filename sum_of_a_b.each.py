str_to_check = str(input().lower())
list_of_words = ["sand", "water", "fish", "sun"]
counter = 0
for word in list_of_words:
    counter += str_to_check.count(word)
print(counter)
