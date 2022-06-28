to_do_notes = input()
to_do_list = ["" for i in range(0, 11)]
while not to_do_notes == "End":
    command = to_do_notes.split("-")
    to_do_list[int(command[0])] = command[1]
    to_do_notes = input()
final_to_do = [task for task in to_do_list if not task == ""]
print(final_to_do)
