book = str(input())
book_counter = 0
while True:
    search = input()
    if search == book:
        print(f"You checked {book_counter} books and found it.")
        break
    elif search == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break
    book_counter += 1


