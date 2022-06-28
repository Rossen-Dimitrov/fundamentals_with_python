key = int(input())
num_lines = int(input())
decrypted = ""
for i in range(num_lines):
    letters = ord(input())
    decrypted += chr(letters + key)
print(decrypted)

