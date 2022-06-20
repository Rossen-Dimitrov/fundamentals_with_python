first_string = input().split(', ')
second_string = input().split(', ')
substrings = []

for f_word in first_string:
    for sec_word in second_string:
        if f_word in sec_word and not f_word in substrings:
            substrings.append(f_word)
print(substrings)
