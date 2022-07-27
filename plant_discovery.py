num_lines = int(input())
plant_dict = dict()

for i in range(num_lines):
    plant, rarity = input().split("<->")
    plant_dict[plant] = {"RARITY": rarity, "RATING": []}

com_in = input()
while not com_in == "Exhibition":
    com_in = com_in.split(": ")
    command = com_in[0]
    if command == 'Rate':
        plant, rating = com_in[1].split(' - ')
        if plant in plant_dict and int(rating) > 0:
            plant_dict[plant]["RATING"].append(int(rating))
        else:
            print("error")
    elif command == 'Update':
        plant, new_rarity = com_in[1].split(' - ')
        if plant in plant_dict:
            plant_dict[plant]["RARITY"] = new_rarity
        else:
            print("error")
    elif command == 'Reset':
        plant = com_in[1]
        if plant in plant_dict:
            plant_dict[plant]["RATING"] = []
        else:
            print("error")

    com_in = input()

print("Plants for the exhibition:")
for plant in plant_dict:
    if plant_dict[plant]['RATING']:
        total_rating = sum(plant_dict[plant]['RATING']) / len(plant_dict[plant]['RATING'])
        print(f"- {plant}; Rarity: {plant_dict[plant]['RARITY']}; Rating: {total_rating:.2f}")
    else:
        print(f"- {plant}; Rarity: {plant_dict[plant]['RARITY']}; Rating: {0:.2f}")
