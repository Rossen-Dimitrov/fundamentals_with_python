username = input()
password = input()

while True:
    user_input = input()
    if password == user_input:
        print(f"Welcome {username}!")
        break
