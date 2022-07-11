data_input = input()
phonebook = {}

while '-' in data_input:
    data_input = data_input.split('-')
    name = data_input[0]
    phone = data_input[1]
    phonebook[name] = phone
    data_input = input()

for name in range(int(data_input)):
    data_input = input()
    if data_input in phonebook:
        print(f"{data_input} -> {phonebook[data_input]}")
    else:
        print(f"Contact {data_input} does not exist.")
