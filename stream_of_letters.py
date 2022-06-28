letter = input()
c_is_marked = False
o_is_marked = False
n_is_marked = False
word = ""
while not letter == "End":
    if (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122):
        if letter == "c":
            if not c_is_marked:
                c_is_marked = True
                letter = ""
            else:
                letter = "c"
        elif letter == "o":
            if not o_is_marked:
                o_is_marked = True
                letter = ""
            else:
                letter = "o"
        elif letter == "n":
            if not n_is_marked:
                n_is_marked = True
                letter = ""
            else:
                letter = "n"
        if c_is_marked and o_is_marked and n_is_marked:
            print(word, end=" ")
            c_is_marked = False
            o_is_marked = False
            n_is_marked = False
            word = ""
        word += letter
    letter = input()

