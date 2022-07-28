raw_key = input()

line_in = input()
while not line_in == "Generate":
    line_in = line_in.split(">>>")
    command = line_in[0]

    if command == "Contains":
        substring = line_in[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        up_low, start, end = line_in[1], int(line_in[2]), int(line_in[3])
        changed = raw_key[start:end]
        if up_low == "Upper":
            changed = changed.upper()
            raw_key = raw_key[:start] + changed + raw_key[end:]
        elif up_low == "Lower":
            changed = changed.lower()
            raw_key = raw_key[:start] + changed + raw_key[end:]
        print(raw_key)

    elif command == "Slice":
        start, end = int(line_in[1]), int(line_in[2])
        raw_key = raw_key[:start] + raw_key[end:]
        print(raw_key)

    line_in = input()
print(f'Your activation key is: {raw_key}')
