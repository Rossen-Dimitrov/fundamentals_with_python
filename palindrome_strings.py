strings = input().split()
searched_palindrome = input()
palindromes = [word for word in strings if word == word[::-1]]

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
