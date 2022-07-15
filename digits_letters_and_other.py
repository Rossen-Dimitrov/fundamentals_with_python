def digits(data):
    return "".join([cha for cha in data if cha.isdigit()])


def letters(data):
    return "".join([str(cha) for cha in data if cha.isalpha()])


def others(data):
    return "".join([str(cha) for cha in data if not cha.isalpha() and not cha.isdigit()])


line_in = input()

print(digits(line_in))
print(letters(line_in))
print(others(line_in))
