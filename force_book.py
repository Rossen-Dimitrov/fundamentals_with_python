force_book = {}
input_line = input()

while not input_line == "Lumpawaroo":
    if ' | ' in input_line:
        input_line = input_line.split(' | ')
        side, user = input_line
        is_not_present = True
        if side not in force_book.keys():
            force_book[side] = []
        for values in force_book.values():
            if user in values:
                is_not_present = False
                break
        if is_not_present:
            force_book[side].append(user)

    elif ' -> ' in input_line:
        input_line = input_line.split(' -> ')
        user, side = input_line
        for key, values in force_book.items():
            if user in values:
                force_book[key].remove(user)
                break
        if side not in force_book.keys():
            force_book[side] = []
        force_book[side].append(user)
        print(f"{user} joins the {side} side!")

    input_line = input()
for side, user in force_book.items():
    if len(force_book[side]) > 0:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for x in user:
            print(f"! {x}")
