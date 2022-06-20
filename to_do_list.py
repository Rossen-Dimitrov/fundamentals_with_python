to_do_list = [''] * 11

command = input()
while not command == "End":
    command = command.split('-')
    importance = int(command[0])
    note = command[1]
    to_do_list[importance] = note

    command = input()
filter_to_do = [n for n in to_do_list if not n == ""]
print(filter_to_do)
