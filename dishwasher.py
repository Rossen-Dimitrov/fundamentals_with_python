bottles_detergent = int(input()) * 750
dishes = 0
pots = 0
counter = 0
data_input = input()
while not data_input == "End":
    counter += 1
    user_input = int(data_input)
    if counter % 3 == 0:
        pots += user_input
        bottles_detergent -= user_input * 15
    else:
        dishes += user_input
        bottles_detergent -= user_input * 5
    if bottles_detergent < 0:
        break
    data_input = input()
if bottles_detergent >= 0:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {bottles_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(bottles_detergent)} ml. more necessary!")