num_pieces = int(input())
pieces_dict = {}

for num in range(num_pieces):
    data = input().split('|')
    piece = data[0]
    composer = data[1]
    key = data[2]
    pieces_dict[piece] = [composer, key]

next_data = input()
while not next_data == "Stop":
    next_data = next_data.split("|")
    command = next_data[0]
    if command == "Add":
        piece, composer, key = next_data[1], next_data[2], next_data[3]
        if piece not in pieces_dict.keys():
            pieces_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command == "Remove":
        piece = next_data[1]
        if piece in pieces_dict.keys():
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        piece, new_key = next_data[1], next_data[2]
        if piece in pieces_dict.keys():
            pieces_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    next_data = input()

for key, value in pieces_dict.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
