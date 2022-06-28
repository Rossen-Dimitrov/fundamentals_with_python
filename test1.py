user_input = str.lower(input())
counter = 0
string_names = ["Water", "Sun", "Fish", "Sand"]
string_list = [i.lower() for i in string_names]
for i in range(4):
    new_string = string_list[i]
    counter += user_input.count(new_string)
print(counter)
