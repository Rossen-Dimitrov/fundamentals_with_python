def validator(password):
    specials = "[@_!#$%^&*()<>?/\\|}{~:\"\']"
    length = False
    digits = False
    special_char = False
    digits_count = 0
    if not any(char in specials for char in password):
        special_char = True
    if 6 <= len(password) <= 10:
        length = True
    for ch in password:
        if ch.isdigit():
            digits_count += 1
    if digits_count > 1:
        digits = True
    return length, digits, special_char


pass_input = input()
length_, digits_, special_char_ = validator(pass_input)
if not length_:
    print("Password must be between 6 and 10 characters")
if not special_char_:
    print("Password must consist only of letters and digits")
if not digits_:
    print('Password must have at least 2 digits')
if length_ and digits_ and special_char_:
    print("Password is valid")
