coded_message = input().split()
secret_message = []

for word in coded_message:
    temp_word = []
    first_letter = ''
    for letter in word:
        if letter.isdigit():
            first_letter += letter
        else:
            temp_word.append(letter)

    temp_word[0], temp_word[-1] = temp_word[-1], temp_word[0]
    temp_word.insert(0, chr(int(first_letter)))
    secret_message.append(''.join(temp_word))

print(' '.join(secret_message))
