stops_string = input()

line_in = input()
while not line_in == "Travel":
    line_in = line_in.split(":")
    command = line_in[0]
    if command == "Add Stop":
        index, city = int(line_in[1]), line_in[2]
        if 0 <= index <= len(stops_string):
            stops_string = stops_string[:index] + city + stops_string[index:]
        print(stops_string)
    elif command == "Remove Stop":
        start, stop = int(line_in[1]), int(line_in[2]) + 1
        if 0 <= start <= stop <= len(stops_string):
            stops_string = stops_string[:start] + stops_string[stop:]
        print(stops_string)
    elif command == "Switch":
        old_string, new_string = line_in[1], line_in[2]
        if old_string in stops_string:
            stops_string = stops_string.replace(old_string, new_string)
        print(stops_string)
    line_in = input()

print(f"Ready for world tour! Planned stops: {stops_string}")
