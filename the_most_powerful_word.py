import math
most_word = ""
most_power = 0
letter_list = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')
while True:
    word = str(input())
    curr_word_power = 0
    if word == "End of words":
        break
    else:
        for letter in word:
            curr_word_power += ord(letter)
    if word[0] in letter_list:
        curr_word_power *= len(word)
    else:
        curr_word_power /= len(word)
    if curr_word_power > most_power:
        most_word = word
        most_power = curr_word_power
print(f"The most powerful word is {most_word} - {math.floor(most_power)}")
