vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
str_to_check = input()
no_vowels = ''.join([char for char in str_to_check if char not in vowels])
print(no_vowels)
