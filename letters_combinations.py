first_letter = str(input())
second_letter = str(input())
except_letter = ord(input())

counter = 0
for char1 in range(ord(first_letter), ord(second_letter) + 1):
    if char1 != except_letter:
        for char2 in range(ord(first_letter), ord(second_letter) + 1):
            if char2 != except_letter:
                for char3 in range(ord(first_letter), ord(second_letter) + 1):
                    if char3 != except_letter:
                        counter += 1
                        print(f'{chr(char1)}{chr(char2)}{chr(char3)}', end=" ")
print(counter)
