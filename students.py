data_in = input()
students = {}

while ":" in data_in:
    data_in = data_in.split(':')
    name = data_in[0]
    stud_id = data_in[1]
    course = data_in[2]
    students[stud_id] = [name, course]

    data_in = input()

for stud_id, values in students.items():
    searched = data_in.replace("_", " ")
    if searched in values:
        print(f"{values[0]} - {stud_id}")