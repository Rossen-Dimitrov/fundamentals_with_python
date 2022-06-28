text = input()
vallue = 0
for letter in text:
    if letter == "a":
        vallue += 1
    elif letter == "e":
        vallue += 2
    elif letter == "i":
        vallue += 3
    elif letter == "o":
        vallue += 4
    elif letter == "u":
        vallue += 5
print(vallue)