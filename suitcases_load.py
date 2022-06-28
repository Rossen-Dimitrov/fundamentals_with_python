trunk_capacity = float(input())
baggage_counter = 0
baggage_volume = 0

while True:
    if baggage_volume == trunk_capacity:
        break
    user_input = input()
    if user_input == "End":
        break
    baggage_counter += 1
    if baggage_counter % 3 == 0:
        baggage_volume += float(user_input) * 1.1
        if baggage_volume > trunk_capacity:
            baggage_counter -= 1
            break
    else:
        baggage_volume += float(user_input)
        if baggage_volume > trunk_capacity:
            baggage_counter -= 1
            break

if trunk_capacity >= baggage_volume:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {baggage_counter} suitcases loaded.")